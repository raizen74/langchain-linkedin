import os
from dotenv import load_dotenv
from langchain.chains import LLMChain  # Chains allow us to combine multiple components together and create one single coherent app
from langchain.prompts import PromptTemplate  # Run the same prompt several times with different inputs
from langchain_openai import ChatOpenAI  # Contains LLMs

# Load environment variables from .env file
load_dotenv()

# Accessing environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

information = """Elon Reeve Musk (born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $254 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attende
"""
#Define the template for the prompt, you can use the same prompt passing different parameters {information} 
summary_template = """
    given the information {information} about a person from I want to you to create:
    1. a short summary
    2. two interesting facts about them
    """
# Wrapper class around the prompt template is the text before injecting the variable
summary_prompt_template = PromptTemplate.from_template(summary_template)
# print(summary_prompt_template)
# temperature decide how creativeness of the model, 0 -> no creative
llm = ChatOpenAI(temperature = 0, model = "gpt-3.5-turbo")  # Chat model is a wrapper around an LLM

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

print(chain.run(information=information))  # What runs the model is always the chain. When we run the chain we pass the input.