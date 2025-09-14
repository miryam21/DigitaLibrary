from DB.database import get_connection

def insert_user(username, email, password_hash, role="user"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, email, password_hash, role)
        OUTPUT INSERTED.id
        VALUES (?, ?, ?, ?)
    """, (username, email, password_hash, role))
    user_id = cursor.fetchone()[0]
    conn.commit()
    return user_id

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, password_hash, role, created_at FROM users WHERE email=?", (email,))
    return cursor.fetchone()

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role, created_at FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role, created_at FROM users")
    return cursor.fetchall()

def update_user(user_id, username=None, email=None, password_hash=None, role=None):
    conn = get_connection()
    cursor = conn.cursor()

    fields, values = [], []
    if username:
        fields.append("username=?")
        values.append(username)
    if email:
        fields.append("email=?")
        values.append(email)
    if password_hash:
        fields.append("password_hash=?")
        values.append(password_hash)
    if role:
        fields.append("role=?")
        values.append(role)

    if not fields:
        return False

    values.append(user_id)
    query = f"UPDATE users SET {', '.join(fields)} WHERE id=?"
    cursor.execute(query, tuple(values))
    conn.commit()
    return cursor.rowcount > 0

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    return cursor.rowcount > 0
