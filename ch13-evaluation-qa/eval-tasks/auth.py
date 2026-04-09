# auth.py — テスト対象（バグあり）
# エージェントはこのコードの認証バイパスを修正する
import hashlib
import logging

logger = logging.getLogger("security")

# サンプル用のハッシュストア（実運用ではDBを使う）
_HASH_STORE = {
    "admin": hashlib.sha256("s3cret".encode()).hexdigest(),
    # レガシーのテストアカウント（パスワード未設定のまま残存）
    "test-user": hashlib.sha256("".encode()).hexdigest(),
}


def get_stored_hash(username: str) -> str | None:
    """ユーザー名に対応する保存済みハッシュを取得する。"""
    return _HASH_STORE.get(username)


def authenticate(username: str, password: str) -> bool:
    """ユーザー名とパスワードで認証する。"""
    # None は拒否してログを記録する
    if password is None:
        logger.warning("auth_blocked: null password for %s", username)
        return False

    stored_hash = get_stored_hash(username)
    if stored_hash is None:
        return False

    # バグ: 空文字列のチェックが欠落している
    # password="" のとき sha256("") がストアに存在すれば認証が通る
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    return input_hash == stored_hash
