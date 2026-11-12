from pydantic import BaseModel, Field
from typing import Dict, Any

class SupportTicketSchema(BaseModel):
    ticket_id: str = Field(..., description="Unique ticket identifier")
    category: str = Field(..., description="Classification category")
    urgency: str = Field(..., pattern="^(low|medium|high|critical)$")
    confidence: float = Field(..., ge=0.0, le=1.0)

def validate_llm_response(raw_json: Dict[str, Any]) -> SupportTicketSchema:
    """Validates LLM dictionary output against strict schema."""
    return SupportTicketSchema(**raw_json)
