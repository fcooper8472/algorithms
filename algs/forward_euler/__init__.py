import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


def insert_hand_sol(t, sol, h, rhs):

    sol_diff = [sol[i] - sol[i-1] for i in range(1, len(sol))]

    st.latex(fr'''
\begin{{aligned}}
y({t[0]:.1f}) &= {sol[0]:.1f} \\
y({t[1]:.1f}) &\approx y({t[0]:.1f}) + {h:.1f}\cdot {rhs}{t[0]:.1f})}} &= {sol[0]:.4f}
{sol_diff[0]:+.4f} &= {sol[1]:.4f} \\
y({t[2]:.1f}) &\approx y({t[1]:.1f}) + {h:.1f}\cdot {rhs}{t[1]:.1f})}} &= {sol[1]:.4f}
{sol_diff[1]:+.4f} &= {sol[2]:.4f} \\
y({t[3]:.1f}) &\approx y({t[2]:.1f}) + {h:.1f}\cdot {rhs}{t[2]:.1f})}} &= {sol[2]:.4f}
{sol_diff[2]:+.4f} &= {sol[3]:.4f} \\
y({t[4]:.1f}) &\approx y({t[3]:.1f}) + {h:.1f}\cdot {rhs}{t[3]:.1f})}} &= {sol[3]:.4f}
{sol_diff[3]:+.4f} &= {sol[4]:.4f} \\
\cdots
\end{{aligned}}
''')


def forward_euler_content():
    st.header('Examples')

    example_dd = st.selectbox(
        label="Pick an example:",
        options=['Example 1', 'Example 2'],
    )

    if example_dd == 'Example 1':
        ivp_latex = r'''y'(t)=e^t,\hspace{12pt}y(0)=1'''
        exact_latex = r'''y(t)=e^t'''
        rhs_hand_str = r'''e^{('''
        init_val = 1.0
        rhs_fun = np.exp
        sol_fun = np.exp
    else:
        ivp_latex = r'''y'(t)=\cos(2t),\hspace{12pt}y(0)=0'''
        exact_latex = r'''y(t)=\frac{1}{2}\sin(2t)'''
        rhs_hand_str = r'''\cos(2\cdot{'''
        init_val = 0.0
        rhs_fun = lambda t: np.cos(2 * t)
        sol_fun = lambda t: 0.5 * np.sin(2 * t)

    st.markdown(r'''Consider the initial value problem''')
    st.latex(ivp_latex)
    st.markdown(r'''with exact solution''')
    st.latex(exact_latex)

    st.subheader('Select a step size h')
    h = st.slider(
        label='',
        min_value=0.1,
        max_value=1.0,
        value=0.5,
        step=0.1,
    )

    t_vals = np.arange(0.0, 4.0 + 1e-12, h)
    exact_sol = sol_fun(t_vals)
    calc_sol = np.zeros(np.shape(t_vals))

    calc_sol[0] = init_val
    for i, _ in enumerate(calc_sol):
        if i == 0:
            continue
        calc_sol[i] = calc_sol[i - 1] + h * rhs_fun(t_vals[i - 1])

    insert_hand_sol(t_vals, calc_sol, h, rhs_hand_str)

    table_data = pd.DataFrame.from_dict({
        'time': t_vals,
        'exact solution': exact_sol,
        'Forward Euler solution': calc_sol,
        'absolute error': np.abs(calc_sol - exact_sol),
    })

    chart_t = np.linspace(0.0, 4.0, 101)
    chart_y = sol_fun(chart_t)

    chart_exact_data = pd.DataFrame.from_dict({
        'series': ['exact solution'] * len(chart_t),
        'time': chart_t,
        'solution': chart_y,
        'abs error': [0] * len(chart_t),
    })

    chart_euler_data = pd.DataFrame.from_dict({
        'series': ['Forward Euler'] * len(calc_sol),
        'time': t_vals,
        'solution': calc_sol,
        'abs error': np.abs(calc_sol - exact_sol),
    })

    line_chart = alt.Chart(pd.concat([chart_exact_data, chart_euler_data])).mark_line().encode(
        x='time',
        y='solution',
        color='series',
        strokeDash=alt.StrokeDash('series', legend=None),
    )

    point_chart = alt.Chart(chart_euler_data).mark_point().encode(
        x='time',
        y='solution',
        color=alt.Color('series', legend=None),
        tooltip=['time', 'solution', 'abs error'],
    )
    point_chart.add_selection(alt.selection_single())

    st.altair_chart((point_chart + line_chart).interactive(), use_container_width=True)
    st.dataframe(table_data)
