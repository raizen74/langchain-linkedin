import warnings

import os
from dotenv import load_dotenv

# Chains allow us to combine multiple components together and create one single coherent app
from langchain.chains import LLMChain

# Run the same prompt several times with different inputs
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Contains LLMs
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

# Deactivate all warnings
warnings.filterwarnings("ignore")
# Load environment variables from .env file
load_dotenv()

# Accessing environment variables
# PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")
# print(PROXYCURL_API_KEY)

print("Hello LangChain")
linkedin_profile_url = linkedin_lookup_agent(name="David Galera Alfaro")

# Define the template for the prompt, you can use the same prompt passing different parameters {information}
summary_template = """
    given the Linkedin information {information} about a person from I want to you to create:
    1. a short summary
    2. two interesting facts about them
    """
# # Wrapper class around the prompt template is the text before injecting the variable
summary_prompt_template = PromptTemplate.from_template(summary_template)
# # print(summary_prompt_template)
# # temperature decide how creativeness of the model, 0 -> no creative
llm = ChatOpenAI(
    temperature=0, model="gpt-3.5-turbo"
)  # Chat model is a wrapper around an LLM

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url=linkedin_profile_url,
)
print(linkedin_data)
print(
    chain.run(information=linkedin_data)
)  # What runs the model is always the chain. When we run the chain we pass the input.

# Agents can make external API calls and access databases, the engine of the agents is an LLM
