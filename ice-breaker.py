from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile_info
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

import os
from dotenv import load_dotenv,dotenv_values


def ice_break_with(name:str) -> str:
    """
    Get the LinkedIn profile URL of a person using the LinkedIn lookup agent.
    
    Args:
        name (str): The full name of the person.
        
    Returns:
        str: The LinkedIn profile URL of the person.
    """
    print("Hello, Ice Breaker!")
    linkedin_profile_name = linkedin_lookup_agent(name=name)

    linkedin_data= scrape_linkedin_profile_info(linkedin_profile_url=linkedin_profile_name, mock=True)

    summary_template = """
    given the LinkedIn information {information} about a person, I want you to crreate 
    1. a short summary of the person
    2. two interesting facts about the person
    """

    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) # instantiate OpenAI LLM
    
    
    # llm = ChatOllama(model="llama3.2", temperature=0) # instantiate Ollama LLM
    # llm= ChatOllama(model="mistral", temperature=0) # instantiate Mistral LLM
    
    
    chain = summary_prompt | llm | StrOutputParser()

    res= chain.invoke(input={"information": linkedin_data})
    
    print(res)


if __name__=="__main__":
    load_dotenv()
    
    ice_break_with(name="Shivajee Gupta")