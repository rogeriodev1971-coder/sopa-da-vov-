import argparse
import json
from pathlib import Path
from typing import Any, Dict, Optional

from sopa_da_vovo.benchmark import BenchmarkTask
from sopa_da_vovo.evaluator import evaluate_response
from sopa_da_vovo.report import export_report


def load_tasks(path: str | Path):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return [
        BenchmarkTask(
            id=item["id"],
            name=item["name"],
            description=item["description"],
            input_text=item["input_text"],
            expected_output=item.get("expected_output"),
        )
        for item in raw
    ]


def load_responses(path: Optional[str | Path]) -> Dict[str, str]:
    if not path:
        return {}

    data = json.loads(Path(path).read_text(encoding="utf-8"))

    if isinstance(data, dict):
        return {str(k): str(v) for k, v in data.items()}

    if isinstance(data, list):
        result = {}
        for item in data:
            key = item.get("task_id") or item.get("id")
            value = item.get("candidate_response") or item.get("response")
            if key is not None:
                result[str(key)] = str(value)
        return result

    raise ValueError("O arquivo de respostas deve ser um dicionário ou uma lista de itens.")


def run_benchmark(tasks_path: str | Path, responses_path: Optional[str | Path] = None, output_path: str | Path = "reports/results.json") -> list[Dict[str, Any]]:
    tasks = load_tasks(tasks_path)
    responses = load_responses(responses_path)

    results = []
    for task in tasks:
        candidate = responses.get(task.id, task.expected_output or task.input_text)
        metrics = evaluate_response(candidate, task.expected_output)
        result = {
            "task_id": task.id,
            "task_name": task.name,
            "description": task.description,
            "status": metrics["status"],
            "similarity": metrics["similarity"],
            "coverage": metrics["coverage"],
            "accuracy": metrics["accuracy"],
        }
        results.append(result)

    export_report(results, output_path)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa benchmark simples para tarefas de IA.")
    parser.add_argument("--tasks", required=True, help="Caminho do arquivo JSON com as tarefas.")
    parser.add_argument("--responses", help="Caminho do arquivo JSON com respostas candidatas por task_id.")
    parser.add_argument("--output", default="reports/results.json", help="Caminho para exportar o relatório final.")
    parser.add_argument("--format", choices=["json", "csv"], default="json", help="Formato do relatório exportado.")
    args = parser.parse_args()

    results = run_benchmark(args.tasks, args.responses, args.output)

    for item in results:
        print(f"Task: {item['task_id']} | status: {item['status']}")
        print(f"  similarity={item['similarity']:.2f} coverage={item['coverage']:.2f} accuracy={item['accuracy']:.2f}")

    print(f"\nRelatório exportado em: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
