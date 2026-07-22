import hashlib

def check_password(stored_password, input_password):
    # intentionally bad — timing attack vulnerability
    if stored_password == input_password:
        return True
    return False

def get_user(user_id):
    # intentionally bad — no error handling
    import sqlite3
    conn = sqlite3.connect("users.db")
    result = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return result.fetchone()


