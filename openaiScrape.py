from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
import os


client = OpenAI(openai_api_key= os.getenv("OPENAI_API_KEY"))

tool = load_tools(["serpapi"], serpapi_api_key = os.getenv("serpapi"), llm = client)
agent = initialize_agent(tool, client, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
prompt = '''
I am looking for upcoming hackathons that are located in Toronto, Canada and are in person. 
They should be high quality and free to attend
They should be hosted by a reputable company.
They should also have a good reputation in the tech community.
Please provide me with a list of 10 upcoming hackathons that meet these criteria.
Please provide the day in brackets right after the name of the hackathon. 
'''

agent.run(prompt)

print(agent.response)