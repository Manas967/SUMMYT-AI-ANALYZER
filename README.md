# 🎥 SUMMYT: AI-Powered YouTube Video Analyzer

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

SUMMYT is a Generative AI web app that extracts transcripts from YouTube videos and uses Google’s Gemini model to generate structured summaries. It also includes an interactive Q&A chat so you can ask questions based strictly on the transcript.

---

## ✨ Key Features
- **Instant Summarization:** Concise overview + key takeaways
- **Interactive Contextual Q&A:** Ask questions strictly based on transcript context
- **Bilingual Support:** English + Hindi
- **Smart Error Handling:** Handles missing/disabled transcripts
- **Optimized Performance:** Session caching to avoid redundant calls

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI/LLM:** Google GenAI SDK (`gemini-2.5-flash`)
- **Transcript:** YouTube Transcript API
- **Env:** `python-dotenv`

---

## 🔐 Environment Variables

Create a `.env` file in the project root (same folder as `app.py`):

```env
GEMINI_API_KEY=Your Api key
```

> Never commit your real API key to GitHub.

---

# ✅ How to Run (2 Ways)

## 1) 🚀 Run Locally (Without Docker)

### Step 1 — Clone the repository
```bash
git clone https://github.com/Manas967/SUMMYT-AI-ANALYZER.git
cd SUMMYT-AI-ANALYZER
```

### Step 2 — Create & activate a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Add `.env`
Create/edit `.env`:
```bash
nano .env
```

Add:
```env
GEMINI_API_KEY=Your Api key
```

### Step 5 — Run the app
```bash
streamlit run app.py
```

Open:
```text
http://localhost:8501
```

---

## 2) 🐳 Run With Docker

### Option A — Docker Compose (Recommended)

This repo includes a `docker-compose.yml` with:
- service name: `summyt`
- container name: `summyt-ai-analyzer`
- port mapping: `8501:8501`
- env var: `GEMINI_API_KEY` loaded from your local `.env`

#### Start (build + run)
```bash
docker compose up -d --build
```

#### View logs
```bash
docker logs -f summyt-ai-analyzer
```

#### Stop
```bash
docker compose down
```

#### Start again (without rebuilding)
```bash
docker compose up -d
```

Open:
```text
http://localhost:8501
```

---

### Option B — Docker CLI (Alternative)

#### Build image
```bash
docker build -t summyt-ai-analyzer .
```

#### Run container (load env from `.env`)
```bash
docker run -d --name summyt-ai-analyzer --env-file .env -p 8501:8501 summyt-ai-analyzer
```

#### Logs / stop / start
```bash
docker logs -f summyt-ai-analyzer
docker stop summyt-ai-analyzer
docker start summyt-ai-analyzer
```

#### Clean restart
```bash
docker rm -f summyt-ai-analyzer
docker run -d --name summyt-ai-analyzer --env-file .env -p 8501:8501 summyt-ai-analyzer
```

---

## 💡 Usage
1. Paste a valid YouTube video URL.
2. Select output language (English / Hindi).
3. Click **"Full info in one tap! 🏎️"** to generate the summary.
4. Use the **Q&A Section** to ask questions about the video content.