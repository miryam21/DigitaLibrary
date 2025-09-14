from queries.loan_queries import (
    insert_loan, get_all_loans, get_loan_by_id, update_loan, delete_loan
)
from models.loan import LoanCreate, LoanUpdate

def create_loan(data: LoanCreate):
    loan_id = insert_loan(data.user_id, data.book_id)
    return {"id": loan_id, "user_id": data.user_id, "book_id": data.book_id, "status": "borrowed"}

def list_loans():
    rows = get_all_loans()
    return [
        {"id": r[0], "user_id": r[1], "book_id": r[2], "borrow_date": r[3], "return_date": r[4], "status": r[5]}
        for r in rows
    ]

def get_loan(loan_id: int):
    row = get_loan_by_id(loan_id)
    if not row:
        return None
    return {"id": row[0], "user_id": row[1], "book_id": row[2], "borrow_date": row[3], "return_date": row[4], "status": row[5]}

def update_loan_service(loan_id: int, data: LoanUpdate):
    ok = update_loan(loan_id, data.return_date, data.status)
    return ok

def delete_loan_service(loan_id: int):
    return delete_loan(loan_id)
