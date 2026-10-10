from pathlib import Path


def test_evaluate_response_basic():
    from sopa_da_vovo.evaluator import evaluate_response

    result = evaluate_response(
        "A empresa lançou um novo produto para automatizar tarefas repetitivas.",
        "A empresa lançou um novo produto para automatizar tarefas repetitivas."
    )

    assert result["status"] == "pass"
    assert result["similarity"] >= 0.9
