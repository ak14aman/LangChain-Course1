from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

def main():
    print("Hello from langchain-course1!")


if __name__ == "__main__":
    main()
