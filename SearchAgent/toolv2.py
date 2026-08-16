# from langchain_tavily import tavily_map
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [TavilySearch()]

agent = create_agent(model=llm,tools=tools)


def main():
    print("hello, I am prasad")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job posting above 10LPA for an ai engineer in the Pune Area on linkedin and list theier details ")})
    print(result)
    
    
if __name__ == "__main__":
    main()

    