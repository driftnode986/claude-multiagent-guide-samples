from auth import authenticate


def test_empty_password_is_rejected():
    """Verify that an empty-string password is rejected."""
    # test-user has a stored hash for the empty string
    result = authenticate("test-user", "")
    assert result is False, "Empty password must not pass authentication"


def test_empty_password_logs_blocked_event(caplog):
    """Verify that an empty-password attempt is recorded in security logs."""
    with caplog.at_level("WARNING", logger="security"):
        authenticate("test-user", "")
    assert any(
        "auth_blocked" in r.message for r in caplog.records
    ), "auth_blocked event not found in logs"
