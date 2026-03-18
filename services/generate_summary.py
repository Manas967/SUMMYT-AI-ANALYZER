from google.genai import types  # type: ignore

from services.llm_config import get_client, system_instruction


def generate_summary(transcript_text: str, target_language: str) -> str:
    """Generate a structured transcript summary in the requested language."""
    client = get_client()
    prompt = f"""
    Analyze the following video transcript and provide a comprehensive summary in {target_language}.
    Structure your response with:
    1. A brief overview (1-2 sentences).
    2. Key Takeaways (in bullet points).

    Transcript:
    {transcript_text}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(system_instruction=system_instruction),
    )
    return response.text
