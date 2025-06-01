# 📄 Resume Analyzer using CrewAI & Gemini 2.0 Flash

This project is an automated resume processing pipeline built using the [CrewAI](https://docs.crewai.com/) framework and Google’s **Gemini 2.0 Flash** LLM. It fetches resumes from Gmail, extracts GitHub links from the resume content, analyzes GitHub profiles, and generates a structured report summarizing each candidate’s technical contributions.

---

## 🚀 Features

* ✅ **Gmail Integration** – Automatically fetch emails containing resumes (PDFs) received today.
* ✅ **Resume Parsing** – Extract GitHub URLs from the downloaded resumes.
* ✅ **GitHub Profile Analysis** – Scrape GitHub profile activity, pull requests, issues, and repositories.
* ✅ **Markdown + DOCX Report** – Outputs a clean, tabular summary of each candidate’s GitHub profile.
* ✅ **Multi-Agent Orchestration** – Built using the CrewAI agent-task framework for clean separation of duties.
* ✅ **Powered by Gemini 2.0 Flash** – Fast, lightweight large language model for factual, structured output.

---

## 📁 Project Structure

```
.
├── .python-version
├── main.py
├── tools.py
├── utils.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── Resumes/                # Auto-created folder for storing downloaded resume PDFs
├── credentials.json        # OAuth 2.0 credentials for Gmail API
├── .env                    # Environment variables including Gemini API key
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install Dependencies (using `uv`)

Make sure [uv](https://github.com/astral-sh/uv) is installed:

```bash
uv pip install -r requirements.txt
```

---

### 3. Enable Gmail API

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or use an existing one.
3. Enable the **Gmail API** for the project.
4. Configure **OAuth consent screen** and download `credentials.json`.
5. Place the `credentials.json` file in the root directory of the project.

On first run, it will ask for permission in the browser and store `token.json` for future sessions.

---

### 4. Add Gemini API Key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your-gemini-api-key
```

You can get the API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

---

### 5. Run the Application

```bash
python main.py
```

It will:

* Search today’s emails for PDF attachments named like resumes.
* Extract GitHub links from those resumes.
* Analyze GitHub profiles using CrewAI + Gemini.
* Generate a `.docx` report with detailed insights.

---

## 🧠 Tech Stack

* **LLM**: [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/)
* **Framework**: [CrewAI](https://docs.crewai.com/)
* **Email**: Gmail API via Google OAuth
* **PDF Processing**: PyMuPDF & PyPDF2
* **GitHub Analysis**: HTML scraping + GitHub stats API
* **Environment Management**: `uv` package manager
* **Output**: Structured `.docx` reports
