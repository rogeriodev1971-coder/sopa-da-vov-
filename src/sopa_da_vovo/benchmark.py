from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BenchmarkTask:
    id: str
    name: str
    description: str
    input_text: str
    expected_output: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class BenchmarkResult:
    task_id: str
    task_name: str
    status: str
    similarity: float
    coverage: float
    accuracy: float
    details: Dict[str, Any] = field(default_factory=dict)


class BenchmarkRunner:
    def __init__(self, tasks: Optional[List[BenchmarkTask]] = None):
        self.tasks = tasks or []

    def add_task(self, task: BenchmarkTask) -> None:
        self.tasks.append(task)

    def run(self) -> List[BenchmarkTask]:
        return self.tasks
