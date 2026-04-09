from auth import authenticate


def test_empty_password_is_rejected():
    """空文字列のパスワードが拒否されることを確認する。"""
    # test-user は空パスワードのハッシュが残存しているアカウント
    result = authenticate("test-user", "")
    assert result is False, "空パスワードで認証が通ってはいけない"


def test_empty_password_logs_blocked_event(caplog):
    """空パスワード試行がセキュリティログに記録されることを確認する。"""
    with caplog.at_level("WARNING", logger="security"):
        authenticate("test-user", "")
    assert any(
        "auth_blocked" in r.message for r in caplog.records
    ), "auth_blockedイベントがログに記録されていない"
