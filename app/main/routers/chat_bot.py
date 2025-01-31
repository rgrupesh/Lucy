import random

from fastapi import status
from fastapi.routing import APIRouter

from app.main.services.intent_classification_service import IntentClassificationService
from app.main.schemas.schemas import GetBotResponseSchema

classification_service = IntentClassificationService()
router = APIRouter(prefix='/bot')


@router.post("/chat", status_code=status.HTTP_200_OK, response_model=GetBotResponseSchema)
def get_bot_response(query: str) -> dict : 
    inp_x=query.lower()
    results = classification_service.predict(inp_x)
    response= classification_service.get_response(results)

    return {"message": random.choice(response)}
