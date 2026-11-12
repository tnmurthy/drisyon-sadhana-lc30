import pytest
from pydantic import ValidationError
from src.chain import validate_llm_response

def test_gate1_valid_schema():
    payload = {"ticket_id": "TCK-101", "category": "billing", "urgency": "high", "confidence": 0.95}
    obj = validate_llm_response(payload)
    assert obj.ticket_id == "TCK-101"
    assert obj.urgency == "high"

def test_gate1_invalid_schema_rejected():
    bad_payload = {"ticket_id": "TCK-102", "category": "billing", "urgency": "extreme", "confidence": 1.5}
    with pytest.raises(ValidationError):
        validate_llm_response(bad_payload)
