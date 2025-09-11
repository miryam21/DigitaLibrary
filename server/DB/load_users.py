from database import get_connection

# רשימת משתמשים ראשוניים
users = [
    ("miri", "miri@example.com", "123456", "admin"),
    ("roni", "roni@example.com", "123456", "user"),
    ("shmuel", "shmuel@example.com", "123456", "user"),
    ("shira", "shira@example.com", "123456", "user"),
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
