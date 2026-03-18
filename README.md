# 🎥 SUMMYT: AI-Powered YouTube Video Analyzer

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

SUMMYT is an advanced Generative AI web application that extracts transcripts from YouTube videos and uses Google's model to generate structured, highly accurate summaries. Beyond just summarizing, it features an interactive Q&A chat, allowing users to ask specific questions about the video's content—all without having to watch a single second.

## ✨ Key Features
* **Instant Summarization:** Distills hours of video content into concise overviews and bulleted key takeaways.
* **Interactive Contextual Q&A:** Chat directly with the video context. Ask specific questions, and the AI will answer based *strictly* on the transcript.
* **Bilingual Support:** Generate notes and receive answers in both **English** and **Hindi**.
* **Smart Error Handling:** Gracefully handles videos with disabled transcripts or missing closed captions.
* **Optimized Performance:** Utilizes session state caching to prevent redundant API calls, keeping the app incredibly fast.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI/LLM:** Google GenAI SDK (`gemini-2.5-flash`)
* **Data Extraction:** YouTube Transcript API
* **Environment Management:** Python `python-dotenv`

---

## 🚀 Local Setup & Installation (Ubuntu/Linux)

Follow these steps to run SUMMYT on your local machine.

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/Manas967/SUMMYT.git
cd SUMMYT
\`\`\`

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
\`\`\`bash
python3 -m venv gemini_env
source gemini_env/bin/activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Configure Environment Variables
Create a \`.env\` file in the root directory to securely store your API key.
\`\`\`bash
nano .env
\`\`\`
Add your Gemini API key to the file:
\`\`\`env
GEMINI_API_KEY="your_actual_api_key_here"
\`\`\`

### 5. Run the Application
\`\`\`bash
streamlit run app.py
\`\`\`
The application will open automatically in your browser at \`http://localhost:8501\`.

---

## 🐳 Docker Setup (Added)

If you are running this project with Docker, use the commands below.

### Build Image
\`\`\`bash
docker build -t my-app .
\`\`\`

### Run Container (Correct Port Mapping)
This app runs on port \`8501\` inside the container, so map host port to \`8501\`.

\`\`\`bash
docker run -d --name summyt-app -p 8501:8501 my-app
\`\`\`

Open in browser:
\`\`\`text
http://localhost:8501
\`\`\`

### If You Stopped the Container and Want to Run Again
If container already exists:

\`\`\`bash
docker start summyt-app
\`\`\`

If you want a clean restart:

\`\`\`bash
docker rm -f summyt-app
docker run -d --name summyt-app -p 8501:8501 my-app
\`\`\`

### Docker Compose (Recommended)
Start:

\`\`\`bash
docker compose up -d --build
\`\`\`

Stop:

\`\`\`bash
docker compose down
\`\`\`

Start again after stop:

\`\`\`bash
docker compose up -d
\`\`\`

### Quick Checks
\`\`\`bash
docker ps
docker logs --tail 50 summyt-ai-analyzer
\`\`\`

---

## 💡 Usage
1. Paste any valid YouTube video URL into the input field.
2. Select your preferred output language (English or Hindi).
3. Click **"Full info in one tap! 🏎️"** to extract the transcript and generate the summary.
4. Once processed, use the **Q&A Section** at the bottom to ask specific questions about the video's content.
