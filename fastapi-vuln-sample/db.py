"""SQLite 시드 — 데모용."""
import sqlite3

DB_PATH = "vuln_shop.db"


def get_conn() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def init_db() -> None:
    conn = get_conn()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id INTEGER PRIMARY KEY, username TEXT, email TEXT, role TEXT, password TEXT)"
    )
    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO users (username, email, role, password) VALUES (?, ?, ?, ?)",
            [
                ("admin", "admin@vuln.shop", "admin", "P@ssw0rd!"),
                ("alice", "alice@vuln.shop", "user", "alicepw"),
                ("bob", "bob@vuln.shop", "user", "bobpw"),
            ],
        )
        conn.commit()
    conn.close()
