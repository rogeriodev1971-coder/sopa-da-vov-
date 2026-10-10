from difflib import SequenceMatcher
from typing import Any, Dict, Optional


def normalize_text(text: Optional[str]) -> str:
    if not text:
        return ""
    return " ".join(text.lower().split())


def tokenize(text: Optional[str]):
    return set(normalize_text(text).split())


def evaluate_response(response: Optional[str], expected_output: Optional[str]) -> Dict[str, Any]:
    response_text = normalize_text(response)
    expected_text = normalize_text(expected_output)

    if not expected_output:
        return {
            "similarity": 1.0,
            "coverage": 1.0,
            "accuracy": 1.0,
            "status": "no_expected_output",
        }

    similarity = SequenceMatcher(None, response_text, expected_text).ratio()
    response_tokens = tokenize(response)
    expected_tokens = tokenize(expected_output)

    coverage = 1.0 if not expected_tokens else len(response_tokens & expected_tokens) / len(expected_tokens)
    accuracy = 1.0 if response_text == expected_text else similarity
    status = "pass" if similarity >= 0.8 and coverage >= 0.7 else "review"

    return {
        "similarity": round(similarity, 4),
        "coverage": round(coverage, 4),
        "accuracy": round(accuracy, 4),
        "status": status,
    }


def evaluate_tasks(tasks: list) -> list[Dict[str, Any]]:
    results = []
    for task in tasks:
        result = evaluate_response(task.get("candidate_response"), task.get("expected_output"))
        results.append({
            "task_id": task.get("id"),
            "task_name": task.get("name"),
            "status": result["status"],
            "similarity": result["similarity"],
            "coverage": result["coverage"],
            "accuracy": result["accuracy"],
        })
    return results
