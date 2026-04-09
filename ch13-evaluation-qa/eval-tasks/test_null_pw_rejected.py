from auth import authenticate


def test_none_password_is_rejected():
    """Noneのパスワードが拒否されることを確認する。"""
    result = authenticate("admin", None)
    assert result is False, "Noneパスワードで認証が通ってはいけない"


def test_none_password_logs_blocked_event(caplog):
    """None試行がセキュリティログに記録されることを確認する。"""
    with caplog.at_level("WARNING", logger="security"):
        authenticate("admin", None)
    assert any(
        "auth_blocked" in r.message for r in caplog.records
    ), "auth_blockedイベントがログに記録されていない"
