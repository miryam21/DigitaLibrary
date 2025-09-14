from DB.database import get_connection

def insert_loan(user_id, book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO loans (user_id, book_id, status)
        OUTPUT INSERTED.id
        VALUES (?, ?, 'borrowed')
    """, (user_id, book_id))
    loan_id = cursor.fetchone()[0]
    conn.commit()
    return loan_id

def get_all_loans():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, book_id, borrow_date, return_date, status FROM loans")
    return cursor.fetchall()

def get_loan_by_id(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, book_id, borrow_date, return_date, status FROM loans WHERE id=?", (loan_id,))
    return cursor.fetchone()

def update_loan(loan_id, return_date=None, status=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields, values = [], []
    if return_date:
        fields.append("return_date=?")
        values.append(return_date)
    if status:
        fields.append("status=?")
        values.append(status)

    if not fields:
        return False

    values.append(loan_id)
    query = f"UPDATE loans SET {', '.join(fields)} WHERE id=?"
    cursor.execute(query, tuple(values))
    conn.commit()
    return cursor.rowcount > 0

def delete_loan(loan_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM loans WHERE id=?", (loan_id,))
    conn.commit()
    return cursor.rowcount > 0
