import pandas as pd
from database import get_connection
from pathlib import Path

def load_books_from_csv(limit=100):
    # מוצא את הנתיב האמיתי של הקובץ books.csv בלי קשר לאיפה מריצים
    base_dir = Path(__file__).resolve().parent.parent   # זה מצביע על ספריית LibraryAI
    file_path = base_dir / "dataset" / "books.csv"

    print(f"📂 Using dataset file: {file_path}")

    # קריאת קובץ ה-CSV
    df = pd.read_csv(file_path)

    # לוקחים רק limit ספרים
    df = df.head(limit)

    conn = get_connection()
    cursor = conn.cursor()

    # 🗑️ מחיקת כל הנתונים מהטבלה
    cursor.execute("DELETE FROM books;")
    # 🔄 Reset של ה-ID (Identity)
    cursor.execute("DBCC CHECKIDENT ('books', RESEED, 0);")
    conn.commit()
    print("🗑️ All existing books deleted and ID reset.")

    # הכנסת ספרים חדשים
    for _, row in df.iterrows():
        title = str(row.get("title", ""))[:500]
        author = str(row.get("authors", ""))[:255]

        # שנה
        year = None
        if not pd.isna(row.get("published_year", None)):
            try:
                year = int(row["published_year"])
            except:
                year = None

        # קטגוריה
        category = None
        if not pd.isna(row.get("categories", None)):
            category = str(row["categories"])[:100]

        # מספר עמודים
        pages = None
        if not pd.isna(row.get("num_pages", None)):
            try:
                pages = int(row["num_pages"])
            except:
                pages = None

        # תיאור ותמונה
        summary = str(row.get("description", "")) if not pd.isna(row.get("description", "")) else None
        cover_url = str(row.get("thumbnail", "")) if not pd.isna(row.get("thumbnail", "")) else None

        try:
            cursor.execute("""
                INSERT INTO books (title, author, year, pages, category, summary, cover_url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, title, author, year, pages, category, summary, cover_url)
        except Exception as e:
            print("❌ Failed to insert row:", title, "-", e)

    conn.commit()
    conn.close()
    print(f"✅ {len(df)} books loaded successfully!")

if __name__ == "__main__":
    load_books_from_csv(limit=100)
