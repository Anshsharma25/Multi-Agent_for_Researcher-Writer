from crewai import Task
from tools import tool
from agents import new_research, new_writer

# Researcher Task
research_task = Task(
    description="Conduct research on the latest advancements in generative AI, including new models, "
                "breakthroughs in efficiency, ethical considerations, and real-world applications. "
                "Summarize findings with references to scientific papers.",
    agent=new_research,
    tools=[tool],
    deadline="24 hours",
    complexity="Advanced",
    expected_output="A structured Markdown document summarizing findings with references."
)

# Writer Task
writing_task = Task(
    description="Write an engaging and structured article based on the research findings. "
                "The article should be targeted at AI enthusiasts and professionals, explaining key advancements in generative AI "
                "with clear examples and references.",
    agent=new_writer,
    tools=[tool],
    context=[research_task],  # ✅ FIXED: Context should be passed as a list
    deadline="48 hours",
    async_execution=False,
    complexity="Medium",
    tone="Professional and informative",
    expected_output="A 1000-1500 word blog post with references and key takeaways."
)
