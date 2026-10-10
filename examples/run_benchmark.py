from pathlib import Path
import json

from sopa_da_vovo.benchmark import BenchmarkTask, BenchmarkRunner
from sopa_da_vovo.evaluator import evaluate_response


ROOT = Path(__file__).resolve().parents[1]
TASKS_FILE = ROOT / "data" / "tasks" / "sample_tasks.json"
LEGAL_TASKS_FILE = ROOT / "data" / "tasks" / "legal_sample_tasks.json"


def load_tasks(path: Path):
    raw = json.loads(path.read_text(encoding="utf-8"))
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


if __name__ == "__main__":
    tasks = load_tasks(TASKS_FILE) + load_tasks(LEGAL_TASKS_FILE)
    runner = BenchmarkRunner(tasks)

    print("Executando benchmark de exemplo...\n")

    for task in runner.tasks:
        candidate_response = task.expected_output or task.input_text
        result = evaluate_response(candidate_response, task.expected_output)
        print(f"Task: {task.id} | {task.name}")
        print(f"  Similaridade: {result['similarity']:.2f}")
        print(f"  Cobertura: {result['coverage']:.2f}")
        print(f"  Precisao: {result['accuracy']:.2f}")
        print(f"  Status: {result['status']}")
        print("-" * 50)
