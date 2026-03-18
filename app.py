import streamlit as st  # type: ignore

from services.answer_user_query import answer_user_query
from services.extract_transcript_details import extract_transcript_details
from services.extract_video_id import extract_video_id
from services.generate_summary import generate_summary

st.set_page_config(page_title="SUMMYT - AI Video Analyzer", page_icon="images/icon.png", layout="wide")
st.title("🎥 Let's see... What's inside the video?")

if "transcript" not in st.session_state:
    st.session_state.transcript = None
if "video_id" not in st.session_state:
    st.session_state.video_id = None

youtube_link = st.text_input("Paste the YouTube Video Link:")

st.markdown("### 🌐 AI response language")
output_language = st.radio("Select response Language:", ["English", "Hindi"], horizontal=True)

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if len(video_id) != 11:
        st.warning("Please enter a valid YouTube video URL.")
        st.stop()
    
    if st.session_state.video_id != video_id:
        st.session_state.transcript = None
        st.session_state.video_id = video_id

    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width=500)

    if st.button("Full info in one tap! 🏎️"):
        with st.spinner("I bet you will not have to see the video in future..."):
            transcript_text = extract_transcript_details(video_id)
            
            if transcript_text:
                st.session_state.transcript = transcript_text
                st.toast("Great! 420 successful", icon="📝")
                try:
                    summary = generate_summary(transcript_text, output_language)
                    st.markdown(f"### 📝 Hahaha! Here it is in ({output_language})")
                    st.write(summary)
                    st.balloons()
                except Exception as exc:
                    st.error(str(exc))

if st.session_state.transcript:
    st.divider()
    st.markdown("### 💬 Something cooking then Ask?")
    st.write("Want to know something specific? Ask a question about the video content.")
    
    user_question = st.text_input("Your Question:")
    
    if st.button("Let's go 🏎️"):
        if user_question:
            with st.spinner("Okay! Let me check..."):
                try:
                    answer = answer_user_query(st.session_state.transcript, user_question, output_language)
                    st.info(answer)
                except Exception as exc:
                    st.error(str(exc))
        else:
            st.warning("Please enter a question.")