# from langchain_tavily import tavily_map
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

tavily = TavilyClient()


@tool
def search(query:str)->str:
    """
    Tool that searches over internet
    Args:
        query: the query to search for
    Returns:
        The search result
    
    """
    print(f"Searching for {query}")
    
    response = tavily.search(query=query)
    
    return response


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]

agent = create_agent(model=llm,tools=tools)


def main():
    print("hello, I am prasad")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job posting for an ai engineer in the Pune Area on linkedin and list theier details ")})
    print(result)
    
    
if __name__ == "__main__":
    main()

    