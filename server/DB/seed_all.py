from init_db import init_db, check_tables
from load_users import insert_users
from load_books import load_books_from_csv
from load_loans import insert_loans
# אם תוסיפי בהמשך events:
# from load_events import insert_events

def seed_all():
    print("🗑️ Resetting database...")
    init_db()

    print("\n👤 Adding users...")
    insert_users()

    print("\n📚 Loading books from dataset...")
    # אפשר לשנות את limit לפי כמה ספרים את רוצה
    load_books_from_csv(limit=20)

    print("\n📖 Adding loans...")
    insert_loans()

    # בעתיד: אם תוסיפי אירועים
    # print("\n📝 Adding events...")
    # insert_events()

    print("\n🔎 Checking final state of tables...")
    check_tables()

    print("\n🎉 Database seeding completed successfully!")

if __name__ == "__main__":
    seed_all()
