from pydantic import BaseModel, Field

class InputText(BaseModel):
    paragraph: str = Field(..., max_length=10000 )
    language: str = Field(defaul="english")
    censorship_character: str = Field(default="*")

class OutputText(BaseModel):
    clean_text: str
    appropriate: bool
    amount_censorship: int