from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Import the service and schema from our mock service file
from .llm_service import LLMService, SymptomCheckResponse 

# --- Initialize Application and Service ---
app = FastAPI(
    title="Healthcare Symptom Checker API (Educational)",
    description="Educational API for symptom analysis using a Mock LLM Service.",
    version="1.0.0")

llm_service = LLMService()

# --- API Request Schema ---
class SymptomInput(BaseModel):
    """Schema for the incoming request body."""
    symptoms: str = Field(..., example="fever, chills, body aches, and persistent dry cough")

# --- API Endpoint ---

@app.post(
    "/api/symptoms/check",
    response_model=SymptomCheckResponse,
    summary="Check symptoms and get probable conditions/next steps.")
def check_symptoms_endpoint(input_data: SymptomInput):
    """
    Accepts symptom text, queries the MOCK LLM service, and returns structured advice.
    """
    if not input_data.symptoms or len(input_data.symptoms.split()) < 3:
        raise HTTPException(
            status_code=400,
            detail="Please provide a more detailed symptom description (at least 3 words)."
        )

    # Call the MOCK LLM service to process the symptoms
    response_data = llm_service.check_symptoms(input_data.symptoms)

    # FastAPI handles the conversion to the SymptomCheckResponse model
    return response_data

# --- Root Endpoint for Health Check ---
@app.get("/", tags=["Health"])
def read_root():
    return {"status": "ok", "service": "Symptom Checker LLM API", "LLM_status": "MOCK Ready"}