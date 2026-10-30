# Skill Bridge AI - Personal Professor / Mentor Agent

**Team:** LOW KEYS  
**Sector:** EdTech & Competency Development Platform

An autonomous, agent-based educational mentor that diagnoses student skill gaps, calibrates learning velocity using assessment data, references live market toolchains, and generates precision roadmaps.

---

## 🏗️ Architecture & Agent Tools

```
Skill Bridge AI Agent Core (agent/core.py)
├── Diagnostic Readiness Tool (tools/data_query.py) ──> data/scores.csv
├── Competency Gap Analyzer   (agent/skill_gap.py)   ──> Gap Matrix
├── Market Intelligence Tool  (tools/web_search.py)  ──> Real-time Toolchains
└── Commitment Calculator     (tools/calculator.py)  ──> Effort Feasibility
```

- **`agent/core.py`**: Central agent coordinator.
- **`agent/skill_gap.py`**: Analyzes prerequisites met vs missing competencies.
- **`agent/llm.py`**: Structured pedagogical curriculum engine with optional Gemini API integration.
- **`tools/data_query.py`**: Queries student assessment scores and assigns educational velocity tiers.
- **`tools/web_search.py`**: Industry market demand, modern toolchains, and portfolio expectations.
- **`tools/calculator.py`**: Compares student study commitment against industry transition benchmarks.
- **`templates/index.html`**: Interactive dark-mode dashboard with telemetry metrics and Markdown export.
- **`app.py`**: Production Flask web application.

---

## 🚀 One-Click Cloud Deployment (No Localhost Required)

### Option 1: Deploy on Render (Recommended & Free)
1. Fork or push this repository to your **GitHub** account.
2. Sign in to [Render.com](https://render.com) (free).
3. Click **New +** > **Web Service**.
4. Connect your GitHub repository.
5. Render will automatically detect `render.yaml` or you can enter:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click **Deploy Web Service** — Render will give you a permanent public URL (e.g., `https://your-app.onrender.com`).

---

### Option 2: Deploy on Vercel
1. Push this repository to GitHub.
2. Go to [Vercel.com](https://vercel.com) and click **Add New Project**.
3. Import your GitHub repository.
4. Vercel automatically uses the included `vercel.json` and deploys your site.

---

### Option 3: Deploy on Railway
1. Push this repository to GitHub.
2. Go to [Railway.app](https://railway.app) and click **New Project** > **Deploy from GitHub repo**.
3. Railway uses the included `Procfile` (`gunicorn app:app`) and deploys instantly.

---

## 💻 Local Development (Optional)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run web application
python app.py
# Server starts at http://127.0.0.1:5000

# 3. Or run command-line interface
python main.py
```
