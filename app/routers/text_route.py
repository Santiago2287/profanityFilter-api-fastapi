from fastapi import APIRouter
from app.models.text_model import InputText, OutputText
from app.services.profanity_engine import proccesing_text

router = APIRouter(prefix="/validation-text",tags=["Text"] )


@router.post("/apply_filtre", response_model=OutputText)
async def apply_filtre(data: InputText):

    result = proccesing_text(data.paragraph, data.censorship_character)
    


    return OutputText(**result)
