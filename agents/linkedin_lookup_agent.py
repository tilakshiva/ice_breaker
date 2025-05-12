import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub  
from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name:str) -> str:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    template= """
    given the full name {name_of_person}, I want you to get me only the linkedIn Profile URL of the person as an answer.
    """

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"],
        template=template,
    )
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linked Profile Page",
            func=get_profile_url_tavily,
            description="Use this tool to get the LinkedIn Profile URL of a person. The input should be the full name of the person.",
        )
    ]

    react_prompt= hub.pull("hwchase17/react")
    agent= create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        # max_iterations=3,
    )

    result= agent_executor.invoke(input={"input":prompt_template.format_prompt(name_of_person=name).to_string()})

    if result and result["output"]:
        linkedin_profile_url= result["output"]
        return linkedin_profile_url

if __name__ == "__main__":
    linkedin_url= lookup(name="Samrat Gupta Bangalore")
    print(linkedin_url)
    