from database import get_connection

def list_loans():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        l.id,
        u.username,
        b.title,
        l.borrow_date,
        l.return_date,
        l.status
    FROM loans l
    LEFT JOIN users u ON l.user_id = u.id
    LEFT JOIN books b ON l.book_id = b.id
    ORDER BY l.borrow_date DESC
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("📚 Active Loans in System:\n")
    if rows:
        for row in rows:
            loan_id, username, title, borrow_date, return_date, status = row
            username = username if username else "❓ Unknown User"
            title = title if title else "❓ Unknown Book"
            print(f"Loan #{loan_id} | {username} → {title} | {status}")
            print(f"   Borrowed: {borrow_date} | Returned: {return_date}\n")
    else:
        print("⚠️ No loans found")

    conn.close()

if __name__ == "__main__":
    list_loans()
