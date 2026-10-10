from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ProjectConfig:
    project_name: str = "sopa-da-vov-"
    environment: str = "development"
    model_name: Optional[str] = None
    tasks_dir: str = "data/tasks"
    output_dir: str = "output"
    metrics: List[str] = field(
        default_factory=lambda: ["accuracy", "coverage", "clarity", "grounding"]
    )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "project_name": self.project_name,
            "environment": self.environment,
            "model_name": self.model_name,
            "tasks_dir": self.tasks_dir,
            "output_dir": self.output_dir,
            "metrics": self.metrics,
        }


DEFAULT_CONFIG = ProjectConfig()
