#include <cmath>
#include <iostream>
#include <vector>
#include <tuple>

template<typename callable>
std::tuple<std::vector<double>, std::vector<double>>
forwardEuler(callable f, double yStart, double tStart, double tStop, double h) {

  const int numTimeSteps = std::ceil((tStop - tStart) / h);

  std::vector<double> solution;
  solution.reserve(numTimeSteps);
  solution.emplace_back(yStart);

  std::vector<double> timePoints;
  timePoints.reserve(numTimeSteps);
  timePoints.emplace_back(yStart);

  for (int i = 1; i < numTimeSteps; ++i) {
    const double tNow = tStart + h * static_cast<double>(i - 1);
    const double yNow = solution.at(i - 1);

    solution.emplace_back(yNow + h * f(tNow, yNow));
    timePoints.emplace_back(tStart + h * static_cast<double>(i));
  }

  return std::make_tuple(timePoints, solution);
}

int main() {

  // Example: f(t,y) = cos(2t)
  auto f = [](double t, double y) { return std::cos(2.0 * t); };
  auto [t, y] = forwardEuler(f, 0.0, 0.0, 4.0, 0.1);

  for (std::size_t i = 0ul; i < t.size(); ++i) {
    std::cout << "t:\t" << t[i] << ",\ty\t" << y[i] << '\n';
  }

  return 0;
}
