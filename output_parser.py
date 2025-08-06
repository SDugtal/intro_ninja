from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field  # ✅ fixed typo: 'pydan-tic' -> 'pydantic'

class Summary(BaseModel):
    summary: str = Field(description="Summary about the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    
    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}

summary_parser = PydanticOutputParser(pydantic_object=Summary)
