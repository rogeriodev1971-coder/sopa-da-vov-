# Sopa da Vovó

Projeto mínimo e funcional para benchmark e avaliação de agentes de IA.

## Objetivo

Criar uma base simples para experimentar:
- tarefas de benchmark;
- critérios de avaliação;
- métricas de qualidade;
- organização de experimentos em IA.

## Estrutura

```text
sopa-da-vov-
├── README.md
├── pyproject.toml
├── requirements.txt
├── data/
│   └── tasks/
│       └── sample_tasks.json
├── examples/
│   └── run_benchmark.py
└── src/
    └── sopa_da_vovo/
        ├── __init__.py
        ├── benchmark.py
        ├── config.py
        └── evaluator.py
```

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso rápido

```bash
python examples/run_benchmark.py
```

## Exemplo de execução

O script cria tarefas de exemplo e calcula métricas de qualidade para uma resposta candidata, incluindo:
- similaridade textual;
- cobertura de tokens;
- precisão de resposta;
- status da tarefa.

## Status

Base funcional e pronta para evoluir com novos casos, testes, métricas e integração com agentes de IA.
