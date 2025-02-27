from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os 
from langchain_google_genai import ChatGoogleGenerativeAI

#calling the gemini model
llm = ChatGoogleGenerativeAI(os.getenv("GOOGLE_API_KEY"), model = "",verbose = True, temperature = 0.5)

#create a new agent for researcher with memroy and venbose 

new_research = Agents(
    role = "researcher",
    goal = "uncovering ground breaking technolgies in {topic}",
    backstory =(
        "Driven by cursoity and the desire to uncover the next big thing in {topic},"
        "I am on a mission to find the most innovative technologies and ideas that will shape the future."
    )
    tools= [],
    llm=llm,
    allow_delegation = True,
    memory = True, 
    verbose = True)

#creating a writer agent for custom tools in responsible in news writing 

new_writer = Agent(
    role = "writer",
    goal = "Narrotor compelling tech stories about {topic}",
    backstory =(
        "As a writer, I am passionate about telling stories that captivate and inspire. "
        "I am on a mission to uncover the latest tech trends and share them with the world through engaging articles."
    )
    tools= [],
    llm=llm,
    allow_delegation = False,
    memory = True, 
    verbose = True)