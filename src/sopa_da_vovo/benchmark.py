from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class BenchmarkTask:
    id: str
    name: str
    description: str
    input_text: str
    expected_output: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class BenchmarkRunner:
    def __init__(self, tasks: Optional[List[BenchmarkTask]] = None):
        self.tasks = tasks or []

    def add_task(self, task: BenchmarkTask) -> None:
        self.tasks.append(task)

    def run(self) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        for task in self.tasks:
            results.append(
                {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "input_text": task.input_text,
                    "expected_output": task.expected_output,
                    "metadata": task.metadata or {},
                }
            )
        return results
