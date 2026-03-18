import os
from functools import lru_cache

from dotenv import load_dotenv  # type: ignore
from google import genai

load_dotenv()

system_instruction = """
You are an expert AI youtube video analyst and educational assistant.
Your goal is to extract key information, provide highly accurate summaries, and answer specific user queries based STRICTLY on the provided video transcript.
If a user asks a question whose answer is not contained in the transcript, politely state that the information is not discussed in the video.
Response should be concise and normal verbals should be used in the response so that it will easy to read as well as understood by the user.
Take your time to give the best response to the user.
"""


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
	"""Create and cache Gemini client only when first required."""
	api_key = os.getenv("GEMINI_API_KEY")
	if not api_key:
		raise ValueError(
			"GEMINI_API_KEY is missing. Add it in .env or pass it in Docker using -e GEMINI_API_KEY=your_key"
		)
	return genai.Client(api_key=api_key)
