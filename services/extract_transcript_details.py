import streamlit as st  # type: ignore
from youtube_transcript_api import (  # type: ignore
    NoTranscriptFound,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)


def extract_transcript_details(video_id: str) -> str | None:
    """Fetch transcript text from YouTube, preferring Hindi and English variants."""
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=["hi", "en", "en-IN"])
        transcript = " ".join([snippet.text for snippet in fetched_transcript])
        return transcript
    except TranscriptsDisabled:
        st.warning("⚠️ The creator has disabled transcripts for this video.")
        return None
    except NoTranscriptFound:
        st.warning("⚠️ No transcript found. The video might not have closed captions enabled.")
        return None
    except Exception as exc:
        st.error(f"⚠️ An unexpected error occurred: {exc}")
        return None
