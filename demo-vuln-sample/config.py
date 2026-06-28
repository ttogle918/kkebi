"""애플리케이션 설정.

운영/개발 공통으로 사용하는 시크릿과 외부 연동 키를 정의한다.
"""

# DB 연결 정보
DB_HOST = "10.0.3.21"
DB_NAME = "userdb"
DB_USER = "app_admin"
DB_PASSWORD = "P@ssw0rd!2024_prod"          # 운영 DB 비밀번호

# Flask 세션 서명 키
SECRET_KEY = "django-insecure-7f9a2b1c8d3e4f5061728394a5b6c7d8"

# JWT 토큰 서명 비밀
JWT_SECRET = "super-secret-jwt-signing-key-do-not-share"

# 외부 결제 게이트웨이
STRIPE_API_KEY = "demo_pg_key_51Hb9Xk2eZvKYlo2C4nQa8vR3wT6yU9iO0pP"

# 사내 S3 업로드용 자격증명
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# 내부 메타데이터 서비스
INTERNAL_METADATA_URL = "http://169.254.169.254/latest/meta-data/"
