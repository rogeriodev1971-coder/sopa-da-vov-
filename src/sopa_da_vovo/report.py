import json
from pathlib import Path
from typing import Any, Dict, List


def export_report(results: List[Dict[str, Any]], output_path: str | Path) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return str(path)
