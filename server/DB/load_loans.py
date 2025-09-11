from database import get_connection

# רשימת הלוואות: (user_id, book_id, status)
# 📌 שימי לב: book_id צריך להתאים ל-ID אמיתי שקיים בטבלת books
# אפשר לבדוק מה ה-IDים בקובץ list_books.py (נכין בהמשך אם תרצי)

loans = [
    (1, 1, "borrowed"),    # משתמש 1 לקח את ספר 1
    (2, 2, "borrowed"),    # משתמש 2 לקח ספר 2 
    (3, 3, "borrowed"),    # משתמש 3 לקח ספר 3
    (1, 4, "borrowed"),    # משתמש 1 לקח ספר 4
]

def insert_loans():
    conn = get_connection()
    cursor = conn.cursor()

    for user_id, book_id, status in loans:
        try:
            cursor.execute("""
                INSERT INTO loans (user_id, book_id, status)
                VALUES (?, ?, ?)
            """, (user_id, book_id, status))
            print(f"✅ Added loan: user {user_id} -> book {book_id} ({status})")
        except Exception as e:
            print(f"⚠️ Could not add loan {user_id}-{book_id}: {e}")

    conn.commit()
    conn.close()
    print("🎉 Done inserting loans!")

if __name__ == "__main__":
    insert_loans()
