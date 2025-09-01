import re
from urllib.parse import urlsplit
from typing import Callable, List, Tuple

SHORTENERS = {
    "bit.ly",
    "t.co",
    "tinyurl.com",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly",
    "cutt.ly",
    "s.id",
}

REGEX = {
    "ip_host": re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$"),
    "punycode": re.compile(r"(^|\.)xn--", re.IGNORECASE),
    "percent": re.compile(r"%[0-9A-Fa-f]{2}"),
    "base64ish": re.compile(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{16,}={0,2}(?![A-Za-z0-9+/=])"),
    "susp_kw": re.compile(
        r"(login|verify|secure|update|confirm|limited|suspend|wallet|invoice|payment|account|gift|free|bonus|urgent|unlock)",
        re.IGNORECASE,
    ),
    "brand_action": re.compile(
        r"(paypal|apple|amazon|microsoft|office365|outlook|facebook|instagram|netflix|dhl|fedex|bank|chase|boa|wellsfargo).*(login|verify|secure|update|confirm)",
        re.IGNORECASE,
    ),
    "susp_ext": re.compile(r"\.(php|asp|aspx|jsp)$", re.IGNORECASE),
    "download_ext": re.compile(r"\.(zip|rar|7z|iso|exe|apk|scr)$", re.IGNORECASE),
}

WEIGHTS = {
    "shortener": 20,
    "punycode": 30,
    "ip_host": 35,
    "userinfo": 25,
    "unusual_port": 10,
    "long_host": 10,
    "long_path": 10,
    "long_query": 10,
    "many_subdomains": 15,
    "digit_ratio": 15,
    "hyphen_ratio": 10,
    "percent_density": 15,
    "base64ish": 15,
    "susp_kw": 10,
    "brand_action": 25,
    "susp_ext": 10,
    "download_ext": 20,
}

SAFE_PORTS = {80, 443, 8080, 8443}


def _ratio(s: str, pred: Callable[[str], bool]) -> float:
    if not s:
        return 0.0
    c = sum(1 for ch in s if pred(ch))
    return c / max(1, len(s))


def score_url(url: str) -> Tuple[str, int, List[str]]:
    s = urlsplit(url)
    host = s.hostname or ""
    port = s.port
    path = s.path or ""
    query = s.query or ""
    netloc = s.netloc or ""

    score = 0
    reasons: List[str] = []

    if host in SHORTENERS:
        score += WEIGHTS["shortener"]
        reasons.append("shortener")

    if REGEX["punycode"].search(host):
        score += WEIGHTS["punycode"]
        reasons.append("punycode")
    if REGEX["ip_host"].match(host):
        score += WEIGHTS["ip_host"]
        reasons.append("ip_host")
    if "@" in netloc:
        score += WEIGHTS["userinfo"]
        reasons.append("userinfo")
    if port and port not in SAFE_PORTS:
        score += WEIGHTS["unusual_port"]
        reasons.append(f"unusual_port:{port}")

    if len(host) > 75:
        score += WEIGHTS["long_host"]
        reasons.append("long_host")
    if len(path) > 60:
        score += WEIGHTS["long_path"]
        reasons.append("long_path")
    if len(query) > 200:
        score += WEIGHTS["long_query"]
        reasons.append("long_query")
    if host.count(".") >= 3:
        score += WEIGHTS["many_subdomains"]
        reasons.append("many_subdomains")

    if _ratio(host, str.isdigit) > 0.30:
        score += WEIGHTS["digit_ratio"]
        reasons.append("digit_heavy_host")
    if _ratio(host, lambda c: c == "-") > 0.30:
        score += WEIGHTS["hyphen_ratio"]
        reasons.append("hyphen_heavy_host")

    pct = REGEX["percent"].findall(url)
    if pct and (len(pct) / max(1, len(url))) > 0.05:
        score += WEIGHTS["percent_density"]
        reasons.append("high_percent_encoding")
    if REGEX["base64ish"].search(query):
        score += WEIGHTS["base64ish"]
        reasons.append("base64_like_param")

    hay = f"{host}{path}{query}"
    if REGEX["susp_kw"].search(hay):
        score += WEIGHTS["susp_kw"]
        reasons.append("suspicious_keywords")
    if REGEX["brand_action"].search(hay):
        score += WEIGHTS["brand_action"]
        reasons.append("brand_action_combo")
    if REGEX["susp_ext"].search(path):
        score += WEIGHTS["susp_ext"]
        reasons.append("suspicious_script_ext")
    if REGEX["download_ext"].search(path):
        score += WEIGHTS["download_ext"]
        reasons.append("download_lure_ext")

    verdict = "safe" if score < 20 else ("suspicious" if score < 50 else "malicious")
    return verdict, score, reasons
