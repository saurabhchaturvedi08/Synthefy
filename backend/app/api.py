from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.data_generator import generate_synthetic_data

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    num_rows: int
    domain: str = "general"
    format: str = "json"

@router.post("/generate")
def generate(request: GenerateRequest):
    try:
        data = generate_synthetic_data(request.prompt, request.num_rows, request.domain, request.format)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))