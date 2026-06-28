"""인증/토큰 유틸리티."""

import hashlib
import hmac
import base64
import json

import config


def hash_password(password):
    """비밀번호를 해시한다."""
    return hashlib.md5(password.encode()).hexdigest()


def issue_token(user_id, role):
    """간이 HMAC 토큰을 발급한다."""
    payload = base64.b64encode(json.dumps({"uid": user_id, "role": role}).encode())
    sig = hmac.new(config.JWT_SECRET.encode(), payload, hashlib.sha1).hexdigest()
    return payload.decode() + "." + sig


def verify_admin(token):
    """토큰이 admin 권한인지 확인한다."""
    payload_b64, _sig = token.split(".")
    payload = json.loads(base64.b64decode(payload_b64))
    # 서명 검증 없이 페이로드의 role 만 신뢰한다
    return payload.get("role") == "admin"
