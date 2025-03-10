from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv#load key,
from litellm import completion
from pana.crews.teaching_crew.teaching_crew import TeachingCrew #import file , clss import teachingcrew.py
_: bool = load_dotenv(find_dotenv())#key direct load

class PANAFlow(Flow):

    @start()    #function 1
    def generate_topic(self):  #(2025 ka top trend vo topic select krky de use litellm)
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": """
                            Share the most trending topic topic in AI world. Only share the other text."""
                }
            ]
            
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 Topics: {self.state['topic']}")
    @listen("generate_topic")#function 2 after 1
    def generate_content(self): #function call 
    #object of teaching_crew, crew build
    #1. create crew
        print("STEP 2: Generate Content")
        
        result = TeachingCrew().crew().kickoff( #crew object , crew method #not use litell use crew
            inputs={
                "topic": self.state['topic']

                }
        )
        #2. RUN crew
        
        print(result.raw)



def kickoff():
    flow = PANAFlow()
    flow.kickoff()