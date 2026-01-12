# Superstore GenBI Agent ⚡

A **Natural Language Business Intelligence Agent** for the Superstore sales dataset. Ask questions in plain English — it generates SQL, queries the data, and returns insights.

**Live demo**: https://superstore-genbi-agent-vgqc76vvevlc5l5qqeyjp4.streamlit.app

## What it does

- Understands natural language (e.g. "Top 5 states by total sales?" or "Who is the top customer? Show name.")
- Builds accurate SQL queries
- Executes against SQLite DB
- Formats responses nicely

Built as a portfolio project for AI in BI roles.

## Tech Stack

- **UI**: Streamlit
- **Agent**: LangChain
- **LLM**: Groq (Llama 3.3 70B)
- **DB**: SQLite (from CSV)

## How to run locally

1. Clone repo
   ```bash
   git clone https://github.com/tekena-manuel/superstore-genbi-agent.git
   cd superstore-genbi-agent

2. Setup Environment
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt	

3. Add groq key

4. run streamlit run app.py
