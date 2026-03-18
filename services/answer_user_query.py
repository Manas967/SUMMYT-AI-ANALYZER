from google.genai import types  # type: ignore

from services.llm_config import get_client, system_instruction


def answer_user_query(transcript_text: str, user_query: str, target_language: str) -> str:
    """Answer user questions using only transcript context in the requested language."""
    client = get_client()
    prompt = f"""
    Based on the following transcript, answer the user's question in {target_language}.
    Question: {user_query}

    Transcript:
    {transcript_text}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(system_instruction=system_instruction),
    )
    return response.text
