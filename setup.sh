#!/bin/bash

# Create the .streamlit directory
mkdir -p ~/.streamlit

# Write the configuration files
echo "\
[general]\n\
email = \"ilyassaden@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

