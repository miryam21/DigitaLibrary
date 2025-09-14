from fastapi import APIRouter, HTTPException
from models.loan import LoanCreate, LoanUpdate
from services.loan_service import (
    create_loan, list_loans, get_loan, update_loan_service, delete_loan_service
)

router = APIRouter(prefix="/loans", tags=["Loans"])

# --- יצירת השאלה חדשה ---
@router.post("/")
def create_loan_route(data: LoanCreate):
    return create_loan(data)

# --- כל ההשאלות ---
@router.get("/")
def list_loans_route():
    return list_loans()

# --- השאלה לפי ID ---
@router.get("/{loan_id}")
def get_loan_route(loan_id: int):
    result = get_loan(loan_id)
    if not result:
        raise HTTPException(status_code=404, detail="Loan not found")
    return result

# --- עדכון השאלה (לדוגמה: החזרה) ---
@router.put("/{loan_id}")
def update_loan_route(loan_id: int, data: LoanUpdate):
    ok = update_loan_service(loan_id, data)
    if not ok:
        raise HTTPException(status_code=404, detail="Loan not found or no changes")
    return {"success": True}

# --- מחיקת השאלה ---
@router.delete("/{loan_id}")
def delete_loan_route(loan_id: int):
    ok = delete_loan_service(loan_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"success": True}
