# -------------------------------------------------------------- #
# Do NOT run files in gemini folders directly for right now
# Run as module: uv run -m gemini.chat
# -------------------------------------------------------------- #
from dotenv import load_dotenv
from config import settings
from google import genai
from google.genai import types

load_dotenv()

# Configure Gemini with modern async client from settings
gemini_key = genai.Client(api_key=settings.GEMINI_API_KEY).aio

async def npc_agent_reply(user_text: str):
    try:
        responce = await gemini_key.models.generate_content(
            model="",
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a friendly NPC in a private group chat."
                    "You are witty and brief."
                    "STRICT RULE: Your response must be between 4 and 5 sentences long."
                ),
                max_output_tokens=300,
                temperature=0.7,
            )
        )
        return responce.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "NPC Agent not working... Try to fix it"
