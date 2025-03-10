from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
@CrewBase #class of crew
class TeachingCrew:
    #1. Agent
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def sehrish(self) -> Agent:
        return Agent(
            config=self.agents_config["sehrish"]
        )

    #2. Task
    @task
    def describe_topic(self) -> Task:
        return Task(
            config=self.tasks_config["describe_topic"]
        )
    #3. crew file m yaha nhi
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,   #  Executes tasks in order based on dependencies
            verbose=True,

        )
    #4. run

