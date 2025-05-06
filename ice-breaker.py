from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile_info


import os
from dotenv import load_dotenv,dotenv_values

if __name__=="__main__":
    load_dotenv()
    print("Hello, Langchain!")
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

    linkedin_data= scrape_linkedin_profile_info(
        linkedin_profile_url="https://www.linkedin.com/in/shivajeegupta/", 
        mock=True)
    
    res= chain.invoke(input={"information": linkedin_data})

    print(res)