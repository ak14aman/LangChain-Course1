# LangChain Practice Project

This is a small project to practice LangChain, the framework for building applications with large language models (LLMs). The goal is to learn the core building blocks by writing small, working examples instead of reading about them.

Created by **Aman**.

## What This Project Covers

- Calling chat models from different providers through one interface
- Writing prompt templates and reusable chains
- Using output parsers to get structured results
- Tracing and debugging runs with LangSmith
- Comparing providers such as OpenAI, Google Gemini, and Groq

## Project Structure

As the project grows, it will be organized roughly like this:

```
langchain-practice/
├── README.md
├── .env                 # API keys (never commit this file)
├── requirements.txt
└── src/
    ├── basic_chat.py    # Calling a model directly
    ├── prompts.py       # Prompt templates
    ├── chains.py        # Combining prompts, models, and parsers
    └── tracing.py       # LangSmith tracing examples
```

## Prerequisites

- Python 3.10 or newer
- An API key from at least one provider:
  - [Google AI Studio](https://aistudio.google.com) for Gemini
  - [Groq Console](https://console.groq.com) for Groq models
  - [LangSmith](https://smith.langchain.com) for tracing (optional)

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

2. Install the packages and go ahead:


## Notes

- Model names change over time. If a model is retired, check the provider's current model list.
- Free tiers have rate limits, so expect occasional `429` errors during heavy testing.
- Never commit API keys to Git. Add `.env` to `.gitignore`.

## Author

Created by **Aman**.