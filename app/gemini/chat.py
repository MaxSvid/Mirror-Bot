# -------------------------------------------------------------- #
# Do NOT run files in gemini folders directly for right now
# Run as module: uv run -m gemini.chat
# -------------------------------------------------------------- #
from dotenv import load_dotenv
import logging

from app.config import settings
from google import genai
from google.genai import types

load_dotenv()

# Configure Gemini with modern async client from settings
if not settings.GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

gemini_client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def npc_agent_reply(user_text: str) -> str:
    """Generate NPC reply using Gemini API with 3-4 sentence limit."""
    try:
        response = await gemini_client.aio.models.generate_content(
            model=settings.gemini.model,
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a friendly NPC in a private group chat. "
                    "You are witty and brief. "
                    "STRICT RULE: Your response must be no more than 3-4 sentences long."
                ),
                max_output_tokens=300,
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        logging.error(f"Gemini API Error: {e}")
        return "🤖 NPC Agent encountered an issue. Please try again later."
