"""사용자 API — SQL_INJECTION / IDOR / XSS 취약 엔드포인트."""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

import db

router = APIRouter()


@router.get("/users/search")
def search_users(q: str = "", sort: str = "username"):
    """사용자 검색. 취약: q·sort를 문자열 연결로 쿼리에 삽입 (SQL_INJECTION)."""
    conn = db.get_conn()
    query = (
        "SELECT username, email FROM users "
        f"WHERE email LIKE '%{q}%' ORDER BY {sort}"
    )
    rows = conn.execute(query).fetchall()
    conn.close()
    return {"results": rows}


@router.get("/users/{user_id}")
def get_user(user_id: str):
    """사용자 단건 조회. 취약: 인가 검증 없이 임의 id 조회 (IDOR) + SQLi."""
    conn = db.get_conn()
    row = conn.execute(
        f"SELECT id, username, email, role FROM users WHERE id = {user_id}"
    ).fetchone()
    conn.close()
    return {"user": row}


@router.get("/greet")
def greet(name: str = "guest"):
    """인사 페이지. 취약: name을 이스케이프 없이 HTML에 반영 (반사형 XSS)."""
    return HTMLResponse(f"<html><body><h1>Hello, {name}!</h1></body></html>")
