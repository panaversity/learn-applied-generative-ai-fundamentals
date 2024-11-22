from crewai import Agent, Task, Crew, Process

def createPoemCrew()->Crew:

    #https://docs.crewai.com/concepts/agents#creating-an-agent
    poem_writer: Agent = Agent(
    role='CrewAI Poem Writer',
    goal="""Generate a funny, light heartedpoem about how CrewAI is
            awesome with a sentence count of {sentence_count}""",
    backstory="""You're a creative poet with a talent for capturing the essence of any topic
        in a beautiful and engaging way. Known for your ability to craft poems that
        resonate with readers, you bring a unique perspective and artistic flair to
        every piece you write."""
    )

    #https://docs.crewai.com/concepts/tasks#creating-a-task
    write_poem: Task = Task(
        description="""Write a poem about how CrewAI is awesome.
        Ensure the poem is engaging and adheres to the specified 
        sentence count of {sentence_count}.""",
        agent=poem_writer,
        expected_output='A beautifully crafted poem about CrewAI, with exactly {sentence_count} sentences.',
    )

    #https://docs.crewai.com/concepts/crews
    return Crew(
                agents=[poem_writer], # Automatically created by the @agent decorator
                tasks=[write_poem], # Automatically created by the @task decorator
                process=Process.sequential,
                verbose=True,
            )
