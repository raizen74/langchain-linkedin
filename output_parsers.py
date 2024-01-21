from langchain.output_parsers import PydanticOutputParser #Defines the schema of the output that we want
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel): #Instances from this class represent answers we get from the LLM
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")

    def to_dict(self):
        return {"summary": self.summary, "facts":self.facts}#This dict will be serIalized to JSON
    
person_intel_parser = PydanticOutputParser(pydantic_object=PersonIntel)
#We plug the output parser in the template, we tell the llm the format of the output