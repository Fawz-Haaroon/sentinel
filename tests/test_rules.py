from app.services.url_detector import score_url


def test_scoring_runs():
    verdict, score, reasons = score_url("https://example.com/login")
    assert verdict in {"safe", "suspicious", "malicious"}
    assert isinstance(score, int)
    assert isinstance(reasons, list)

