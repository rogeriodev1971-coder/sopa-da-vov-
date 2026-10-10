# Sopa da Vovó

Projeto mínimo e funcional para benchmark e avaliação de agentes de IA.

## Objetivo

Criar uma base simples para experimentar tarefas, métricas e organização de avaliação de respostas.

## Estrutura

```text
sopa-da-vov-
├── README.md
├── pyproject.toml
├── requirements.txt
└── src/
    └── sopa_da_vovo/
        ├── __init__.py
        ├── config.py
        └── benchmark.py
```

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso básico

```bash
python - <<'PY'
from sopa_da_vovo.benchmark import BenchmarkTask, BenchmarkRunner

tasks = [
    BenchmarkTask(
        id='demo-1',
        name='tarefa-demo',
        description='Exemplo mínimo',
        input_text='Texto de entrada de exemplo',
        expected_output='Texto esperado'
    )
]

print(BenchmarkRunner(tasks).run())
PY
```

## Status

Base funcional e pronta para evoluir com novas tarefas, métricas e experimentos.
