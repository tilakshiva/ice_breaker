from typing import Any, List, Dict
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    """
    A class to represent a summary of a person.
    
    Attributes:
        summary (str): A short summary of the person.
        facts (List[str]): A list of interesting facts about the person.
    """
    summary: str = Field(description="A short summary of the person.")
    facts: List[str] = Field(description="A list of interesting facts about the person.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Summary object to a dictionary.
        
        Returns:
            dict: A dictionary representation of the Summary object.
        """
        return {
            "summary": self.summary,
            "facts": self.facts
        }

summary_Parser = PydanticOutputParser(pydantic_object=Summary)


