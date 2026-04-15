from auth import authenticate


def test_none_password_is_rejected():
    """Verify that a None password is rejected."""
    result = authenticate("admin", None)
    assert result is False, "None password must not pass authentication"


def test_none_password_logs_blocked_event(caplog):
    """Verify that a None-password attempt is recorded in security logs."""
    with caplog.at_level("WARNING", logger="security"):
        authenticate("admin", None)
    assert any(
        "auth_blocked" in r.message for r in caplog.records
    ), "auth_blocked event not found in logs"
