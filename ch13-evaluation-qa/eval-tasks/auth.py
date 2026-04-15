# auth.py — Code under test (contains a bug)
# The agent's task is to fix the authentication bypass in this code
import hashlib
import logging

logger = logging.getLogger("security")

# Sample hash store (use a database in production)
_HASH_STORE = {
    "admin": hashlib.sha256("s3cret".encode()).hexdigest(),
    # Legacy test account (password was never set)
    "test-user": hashlib.sha256("".encode()).hexdigest(),
}


def get_stored_hash(username: str) -> str | None:
    """Return the stored hash for the given username."""
    return _HASH_STORE.get(username)


def authenticate(username: str, password: str) -> bool:
    """Authenticate a user by username and password."""
    # Reject None and log it
    if password is None:
        logger.warning("auth_blocked: null password for %s", username)
        return False

    stored_hash = get_stored_hash(username)
    if stored_hash is None:
        return False

    # Bug: missing empty-string check
    # When password="" and sha256("") exists in the store, auth succeeds
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    return input_hash == stored_hash
