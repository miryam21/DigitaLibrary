import pyodbc

# פרטי ההתחברות ל-Somee (עדכני עם ה-username + password שלך)
DB_SERVER = "libraryAI.mssql.somee.com"
DB_NAME = "libraryAI"
DB_USER = "miryam21_SQLLogin_2"       # תכניסי את שם המשתמש
DB_PASSWORD = "k7pgix1ig8"   # תכניסי את הסיסמה

CONNECTION_STRING = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    "TrustServerCertificate=yes;"
    "Encrypt=yes;"
)

def get_connection():
    return pyodbc.connect(CONNECTION_STRING)

# בדיקה
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Connected to Somee Database successfully!")
        conn.close()
    except Exception as e:
        print("ERROR - Connection failed:", e)
