#https://serper.dev/
# from dotenv import load_dotenv
# load_dotenv()

import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# Retrieve API Key
serper_api_key = os.getenv("SERPER_API_KEY")

# Ensure the API key is set
if not serper_api_key:
    raise ValueError("SERPER_API_KEY is missing. Check your .env file.")

# Initialize SerperDevTool with API Key
tool = SerperDevTool(api_key=serper_api_key)
