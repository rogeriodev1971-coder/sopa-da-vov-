import csv
import json
from pathlib import Path
from typing import Iterable, List, Dict, Any


def export_report(results: List[Dict[str, Any]], output_path: str | Path, file_format: str = "json") -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if file_format == "json":
        path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        return str(path)

    if file_format == "csv":
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["task_id", "task_name", "description", "status", "similarity", "coverage", "accuracy"],
            )
            writer.writeheader()
            for row in results:
                writer.writerow(row)
        return str(path)

    raise ValueError(f"Formato não suportado: {file_format}")
