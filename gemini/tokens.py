# -------------------------------------------------------------- #
# Have an idea to use it for OOP Programming to work with API keys
# For checking different paramaters, tests and results...
# -------------------------------------------------------------- #

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ----------------------------------------------------- #
# 1. Check your text for tokens
# ----------------------------------------------------- #

prompt_input = input(f"Enter your prompt:")

# ----------------------------------------------------- #
# 2. Checking how much tokens in prompt from promp_input
# ----------------------------------------------------- #

print("\n----> USER INPUT <----")
print(prompt_input)