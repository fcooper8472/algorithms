mkdir -p ~/.streamlit/
printf "[general]\nemail=\"fcooper8472@gmail.com\"\n" > ~/.streamlit/credentials.toml
printf "[server]\nheadless=true\nenableCORS=false\nport=%s\n" "${PORT}" > ~/.streamlit/config.toml
