"""vuln-shop API — DAST 데모용 의도적 취약 FastAPI 앱.

api_discovery_node 가 routes/ 하위 @router.* 데코레이터를 엔드포인트로 발견한다.
각 엔드포인트는 DAST executor(SQL_INJECTION/SSRF/XSS/IDOR/AUTH_BYPASS)로 실제
익스플로잇 가능하도록 의도적으로 취약하게 작성됨. 운영 사용 금지.
"""
import os

import uvicorn
from fastapi import FastAPI

import db
from routes import users, proxy

app = FastAPI(title="vuln-shop API", description="DAST 데모용 취약 앱")

db.init_db()
app.include_router(users.router)
app.include_router(proxy.router)


@app.get("/")
def root():
    return {
        "service": "vuln-shop",
        "endpoints": [
            "/users/search?q=&sort=",   # SQL_INJECTION
            "/users/{user_id}",          # IDOR
            "/greet?name=",              # XSS (reflected)
            "/fetch?url=",               # SSRF
            "/ping?host=",               # COMMAND_INJECTION
        ],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
