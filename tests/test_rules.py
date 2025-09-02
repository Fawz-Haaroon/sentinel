from app.core.services.detect import detect_url


def test_scoring_runs() -> None:
    verdict, score, reasons = detect_url("https://example.com/login")
    assert verdict in {"safe", "suspicious", "malicious"}
    assert isinstance(score, int)
    assert isinstance(reasons, list)
