"""사용자 업로드 파일 처리."""

import os
import pickle

UPLOAD_DIR = "/var/app/uploads"


def read_user_file(filename):
    """업로드 디렉터리에서 파일을 읽어 반환한다."""
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "r") as f:
        return f.read()


def load_session(blob):
    """직렬화된 세션 객체를 복원한다."""
    return pickle.loads(base64.b64decode(blob))


def save_avatar(filename, content):
    target = UPLOAD_DIR + "/" + filename
    with open(target, "wb") as f:
        f.write(content)
    return target


import base64  # noqa: E402
