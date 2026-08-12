# import os
# from dotenv import load_dotenv

# load_dotenv()

# print("Tracing:", os.environ.get("LANGSMITH_TRACING"))
# print("Project:", os.environ.get("LANGSMITH_PROJECT"))
# print("Endpoint:", os.environ.get("LANGSMITH_ENDPOINT"))
# print("Key exists:", bool(os.environ.get("LANGSMITH_API_KEY")))

# from dotenv import load_dotenv
# from langsmith import Client

# load_dotenv()

# client = Client()

# projects = list(client.list_projects(limit=5))

# print(projects)

import langsmith as ls
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

joke_template = """
    Tell me a joke about {topic}
"""

prompt = PromptTemplate(
    input_variables=["topic"], template=joke_template
)

llm = ChatOpenAI(temperature=1, model="gpt-5-nano")

chain = prompt | llm



with ls.tracing_context(enabled=True):
    response = chain.invoke(input={"topic":"Gaming"})
    print(response)



# with ls.tracing_context(enabled=True):
#     chain.invoke({"question":"Am i using a callback?","context":"I am using a callback."})