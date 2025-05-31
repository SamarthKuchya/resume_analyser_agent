# 📅 AI Resume Screener with GitHub Analyzer

> **Automated Resume Screening Meets GitHub Intelligence**

An end-to-end AI agent system built using **CrewAI** and **Gemini 2.5**. It automates screening resumes from Gmail, extracting GitHub links, analyzing profiles, and generating Markdown reports.

---

## 🚀 Features

* ✉️ Fetches today’s emails from Gmail
* 🔗 Downloads resume attachments (PDF, DOCX)
* 🤖 Extracts GitHub links using Gemini 2.5
* 📊 Analyzes GitHub contributions and repo stats
* 📄 Generates individual and aggregate Markdown reports
* 🤷 Modular architecture with CrewAI agents
* 💻 Python-based, easy to extend

---

## 🛠️ Tech Stack

| Tool                 | Role                           |
| -------------------- | ------------------------------ |
| **Python**           | Core programming language      |
| **CrewAI**           | Agent orchestration            |
| **Gemini 2.5**       | LLM text extraction & analysis |
| **Gmail API**        | Fetch emails & attachments     |
| **PDFMiner/PyMuPDF** | Resume parsing                 |
| **BeautifulSoup**    | GitHub scraping                |
| **Markdown**         | Report formatting              |
| **Pandas**           | Data processing                |

---

## 📂 Project Structure

```bash
agents/
├── gmail_agent.py       # Gmail email & attachment handling
├── extraction_agent.py  # GitHub link extraction via Gemini
├── github_agent.py      # GitHub profile analyzer
└── report_agent.py      # Markdown report generator

data/
├── resumes/             # Downloaded resumes
└── reports/             # Generated reports

config/
└── credentials.json     # API keys and configs

main.py                  # Entry point for the pipeline
requirements.txt         # Python dependencies
README.md                # Project documentation
```

---

## 🧲 How It Works

1. Run `main.py` to start the pipeline.
2. **Gmail Agent** downloads today’s resume attachments.
3. **Extraction Agent** uses Gemini 2.5 to find GitHub URLs.
4. **GitHub Agent** scrapes public GitHub data (commits, repos, languages).
5. **Report Agent** generates detailed Markdown summaries per candidate.

---

## ✅ Prerequisites

* Python 3.10+
* Gmail API credentials
* Gemini API key
* Public GitHub profiles

---

## 🔧 Setup

```bash
git clone https://github.com/your-username/ai-resume-github-screener.git
cd ai-resume-github-screener
pip install -r requirements.txt
cp config/sample.credentials.json config/credentials.json
# Add your Gmail and Gemini API keys to config/credentials.json
```

---

## 🚦 Usage

```bash
python main.py
```

Reports will be saved to `data/reports/`

---

## 📊 Sample Markdown Report

```markdown
## Candidate: John Doe

- **GitHub:** https://github.com/johndoe  
- **Top Languages:** Python, JavaScript  
- **Public Repos:** 12  
- **Commits (Last Year):** 620  
- **Key Projects:**  
  - AutoML-Pipeline (⭐ 103)  
  - Flask-GPT-Bot (⭐ 85)  

**Insight:** Consistent contributor with strong ML and automation focus.
```

---

## 🧹 Extending

* 📈 LinkedIn scraping integration
* ⭐ LLM-based candidate scoring
* 📃 Database backend for candidate info
* 🎨 Streamlit dashboard for recruiters

---

## 🤝 Contributions

Feel free to open issues or submit pull requests to improve this project.

---

## 📄 License

**MIT License** — See LICENSE file.

---

## 🙏 Acknowledgements

* CrewAI
* Gemini 2.5
* LangChain
* OpenAI
