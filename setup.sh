mkdir -p ~/.streamlit/
echo "[general]\nemail = \"fcooper8472@gmail.com\"\n" > ~/.streamlit/credentials.toml
echo "[server]\nheadless = true\nenableCORS=false\nport = $PORT\n" > ~/.streamlit/credentials.toml
