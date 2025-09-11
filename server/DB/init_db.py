from database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # קודם מוחקים את הטבלאות לפי סדר תלות
    cursor.execute("IF OBJECT_ID('loans', 'U') IS NOT NULL DROP TABLE loans")
    cursor.execute("IF OBJECT_ID('events', 'U') IS NOT NULL DROP TABLE events")
    cursor.execute("IF OBJECT_ID('books', 'U') IS NOT NULL DROP TABLE books")
    cursor.execute("IF OBJECT_ID('users', 'U') IS NOT NULL DROP TABLE users")

    # יצירת טבלת users
    cursor.execute("""
    CREATE TABLE users (
        id INT IDENTITY(1,1) PRIMARY KEY,
        username NVARCHAR(100) UNIQUE NOT NULL,
        email NVARCHAR(255) UNIQUE NOT NULL,
        password_hash NVARCHAR(255) NOT NULL,
        role NVARCHAR(50) DEFAULT 'user',
        created_at DATETIME DEFAULT GETDATE()
    )
    """)

    # יצירת טבלת books (כולל pages ו-category)
    cursor.execute("""
    CREATE TABLE books (
        id INT IDENTITY(1,1) PRIMARY KEY,
        title NVARCHAR(500) NOT NULL,
        author NVARCHAR(255),
        year INT NULL,
        pages INT NULL,
        category NVARCHAR(100),
        summary NVARCHAR(MAX),
        cover_url NVARCHAR(500),
        created_at DATETIME DEFAULT GETDATE()
    )
    """)

    # יצירת טבלת loans
    cursor.execute("""
    CREATE TABLE loans (
        id INT IDENTITY(1,1) PRIMARY KEY,
        user_id INT FOREIGN KEY REFERENCES users(id),
        book_id INT FOREIGN KEY REFERENCES books(id),
        borrow_date DATETIME DEFAULT GETDATE(),
        return_date DATETIME NULL,
        status NVARCHAR(50) DEFAULT 'borrowed'
    )
    """)

    # יצירת טבלת events
    cursor.execute("""
    CREATE TABLE events (
        id INT IDENTITY(1,1) PRIMARY KEY,
        event_type NVARCHAR(100),
        user_id INT NULL,
        book_id INT NULL,
        timestamp DATETIME DEFAULT GETDATE()
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Tables dropped and recreated successfully!")


def check_tables():
    conn = get_connection()
    cursor = conn.cursor()

    tables = ["users", "books", "loans", "events"]

    for table in tables:
        print(f"\n🔎 Checking table: {table}")
        try:
            cursor.execute(f"SELECT TOP 5 * FROM {table}")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("⚠️ Table is empty")
        except Exception as e:
            print(f"❌ Error checking {table}: {e}")

    conn.close()


if __name__ == "__main__":
    init_db()
    check_tables()
