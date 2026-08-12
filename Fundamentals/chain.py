import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()


def main():

    info_path = os.path.join(os.path.dirname(__file__), "info.txt")

    with open(info_path, "r", encoding="utf-8") as file:
        information = file.read()

    summary_template = """
    given the information {information} about a person I want you to create
    1. A short Summary
    2. Two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=1, model="gpt-5-nano")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
