"""프록시/유틸 API — SSRF / COMMAND_INJECTION 취약 엔드포인트."""
import subprocess

import requests
from fastapi import APIRouter

router = APIRouter()


@router.get("/fetch")
def fetch(url: str):
    """원격 리소스 프록시. 취약: 사용자 URL을 검증 없이 요청 (SSRF)."""
    resp = requests.get(url, timeout=5)
    return {"status": resp.status_code, "body": resp.text[:500]}


@router.get("/ping")
def ping(host: str = "127.0.0.1"):
    """호스트 연결성 점검. 취약: host를 shell로 전달 (COMMAND_INJECTION)."""
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return {"output": output.decode(errors="ignore")}
