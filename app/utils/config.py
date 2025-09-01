from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import yaml

DEFAULTS = {
    "thresholds": {"safe": 20, "malicious": 50},
    "shorteners": [
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
    ],
}


def load_yaml(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        return {}
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

