from passlib.context import CryptContext

from database import get_connection

# רשימת משתמשים ראשוניים
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd = pwd_context.hash('1234567a')
users = [
    ("miri", "miri@example.com", pwd, "admin"),
    ("roni", "roni@example.com", pwd, "user"),
    ("shmuel", "shmuel@example.com", pwd, "user"),
    ("shira", "shira@example.com", pwd, "user"),
]

def insert_users():
    conn = get_connection()
    cursor = conn.cursor()

    for username, email, password, role in users:
        try:
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, role)
                VALUES (?, ?, ?, ?)
            """, (username, email, password, role))
            print(f"✅ Added user: {username}")
        except Exception as e:
            print(f"⚠️ Could not add {username}: {e}")

    conn.commit()
    conn.close()
    print("🎉 Done inserting users!")

if __name__ == "__main__":
    insert_users()
