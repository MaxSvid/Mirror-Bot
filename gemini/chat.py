# -------------------------------------------------------------- #
# Do NOT run files in gemini folders directly for right now
# Run as module: uv run -m gemini.chat
# -------------------------------------------------------------- #
import os
from dotenv import load_dotenv
from config import settings

load_dotenv()

# Testing key, only runs inside this file:
if __name__ == "__main__":
    try:
        GEMINI_KEY = settings.GEMINI_API_KEY
        if GEMINI_KEY:
            print(f"Here is {GEMINI_KEY}")
        else:
            raise ValueError("GEMINI_API_KEY not found in .env file")
    except Exception as e:
        print(f"Error occured {e}")
