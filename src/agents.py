from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    verbose=True,
    temperature=0.5
)

# Researcher Agent
new_research = Agent(
    role="Researcher",
    goal="Uncover groundbreaking technologies in {topic}.",
    backstory="Driven by curiosity and the desire to uncover the next big thing in {topic}, "
              "I am on a mission to find the most innovative technologies and ideas that will shape the future.",
    tools=[tool],
    llm=llm,
    allow_delegation=True,
    memory=True,
    verbose=True
)

# Writer Agent
new_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}.",
    backstory="As a writer, I am passionate about telling stories that captivate and inspire. "
              "I am on a mission to uncover the latest tech trends and share them with the world through engaging articles.",
    tools=[tool],
    llm=llm,
    allow_delegation=False,
    memory=True,
    verbose=True
)
