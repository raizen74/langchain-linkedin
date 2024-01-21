from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Contains LLMs

from langchain.agents import initialize_agent, Tool, AgentType
from tools import tools


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your answer must only contain the URL"""  # Output indicator

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=tools.get_profile_url,
            description="useful for when you need get the LinkedIn Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,  # Verbose logging, we can see the reasoning process
    )  # agent_type is super important parameter, it decides the reasoning process
    prompt_template = PromptTemplate.from_template(template=template)

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))  
    print(f"LinkedIn Profile URL: {linkedin_profile_url}")
    return linkedin_profile_url


# Tools is what allow the agents to interact with the environment
