# 🥷 Intro Ninja

Master the art of perfect introductions with **Intro Ninja**, a Gen AI project powered by **Gemini 1.5 Flash** and **LangChain**. Generate personalized conversation starters and insights by analyzing LinkedIn profiles and more.  

![Intro Ninja Demo](static/demo.gif)

[![LangChain](https://img.shields.io/badge/LangChain-🦜🔗-brightgreen)](https://langchain.com/)  
[![Gemini 1.5 Flash](https://img.shields.io/badge/Gemini-1.5%20Flash-blue)](https://ai.google.com/gemini/)  
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.0+-red)](https://flask.palletsprojects.com/)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🎯 Overview

**Intro Ninja** is a generative AI-powered web app that builds smart ice breakers by:
- Locating LinkedIn profiles using **Tavily**
- Analyzing profile data with **LangChain**
- Generating intros using the **Gemini 1.5 Flash** LLM
- Serving results via a clean **Flask** interface

No prior social media overhead needed—just enter a name and get personalized ice breakers instantly.

---

## ✨ AI Pipeline Flow

1. 🔍 **Profile Discovery**: Intelligent LinkedIn lookup via Tavily  
2. 🧠 **Data Extraction**: Scrape profile details with third-party scrapers  
3. 🤖 **AI Processing**: Use Gemini 1.5 Flash + LangChain to analyze and summarize  
4. ✍️ **Intro Generation**: Create conversation starters tailored to the person's background  
5. 💬 **User Interface**: Cloud-hosted Flask frontend for smooth interaction  

---

## 🛠️ Tech Stack

| Component          | Technology                | Purpose                                       |
|-------------------|---------------------------|-----------------------------------------------|
| 🖥️ Frontend         | Flask                     | Web UI and interaction                        |
| 🧠 AI Framework     | LangChain 🦜🔗             | Orchestrates prompts, agents, and chains      |
| 🔍 Profile Discovery| Tavily                    | External search for LinkedIn profiles         |
| 📇 Data Scraping    | Custom Scraper / SDK      | Extracts structured profile data              |
| 🐦 Social Media     | Twitter API (future)      | Social insights and topics (planned)          |
| 🤖 LLM             | Gemini 1.5 Flash          | Generates summaries, facts & intros           |
| 📊 Monitoring       | LangSmith (optional)      | Tracing and debugging of LangChain pipelines  |
| 🐍 Backend         | Python 3.8+                | Glue code and server logic                     |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher  
- Gemini API key (`GEMINI_API_KEY`)  
- Tavily (or search) capabilities  

### Setup and Run

```bash
# Clone the repository
git clone https://github.com/SDugtal/intro_ninja.git
cd intro_ninja

# Install dependencies
pip install -r requirements.txt

# Add environment key
echo "GEMINI_API_KEY=YOUR_KEY_HERE" > .env

# Start the server
python app.py