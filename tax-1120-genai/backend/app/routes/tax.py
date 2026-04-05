from fastapi import APIRouter
from app.models.request_models import NLQRequest
from app.services.llm_parser import parse_nlq
from app.services.tax_engine import calculate_1120_tax
from app.services.summary_service import generate_summary

# ✅ THIS LINE IS CRITICAL
router = APIRouter()

@router.post("/1120-tax")
def estimate_tax(req: NLQRequest):

    structured = parse_nlq(req.query)

    result = calculate_1120_tax(structured)

    summary = generate_summary(structured, result)

    return {
        "input": structured,
        "result": result,
        "summary": summary
    }