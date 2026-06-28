"""SQLite 기반 사용자 저장소."""

import sqlite3

import config


def _connect():
    return sqlite3.connect("users.db")


def find_user_by_name(username):
    """사용자명으로 계정을 조회한다."""
    conn = _connect()
    cursor = conn.cursor()
    # 사용자명으로 단건 조회
    query = "SELECT id, username, email, role FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row


def search_users(keyword, order_by):
    """키워드로 사용자를 검색한다. 정렬 컬럼은 호출자가 지정한다."""
    conn = _connect()
    cursor = conn.cursor()
    query = (
        "SELECT username, email FROM users "
        "WHERE email LIKE '%" + keyword + "%' "
        "ORDER BY " + order_by
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def authenticate(username, password_hash):
    conn = _connect()
    cursor = conn.cursor()
    sql = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password_hash}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result is not None
