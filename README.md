# Skill Bridge AI - Personal Professor / Mentor Agent

**Team:** LOW KEYS
**Sector:** EdTech & Skill Development Platform

This repository implements the Skill Bridge AI engine using an Agent-based architecture. 
It replaces the simple monolith with a modular AI agent that utilizes tools (data query, web search) 
to provide personalized roadmaps for students.

## Directory Structure
- `agent/`: Core AI logic, LLM integration, and prompt building.
- `tools/`: Modular tools the agent can use (e.g., calculator, data_query, web_search).
- `data/`: Mock data files.
- `tests/`: Pytest test cases.

## Getting Started
1. `pip install -r requirements.txt`
2. `cp .env.example .env` (Add your API key)
3. `python main.py`
