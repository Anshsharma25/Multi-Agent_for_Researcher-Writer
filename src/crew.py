from crewai import Crew, Process
from agents import new_research, new_writer
from tasks import research_task, writing_task

# Initialize Crew
crew = Crew(
    agents=[new_research, new_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential
)

# Run Crew AI with the correct syntax
result = crew.kickoff({"topic": "generative AI"})  # ✅ FIXED: Removed `input=`
print(result)
