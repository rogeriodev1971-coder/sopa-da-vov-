# Sopa da Vovó

Projeto base para avaliação de agentes de IA com foco em benchmark, métricas e tarefas de exemplo.

## Objetivo

Cria uma estrutura simples, reutilizável e fácil de evoluir para:
- benchmark de respostas de IA;
- avaliação de qualidade por tarefa;
- comparação de saídas esperadas vs. geradas;
- organização de experiências em IA e automação.

## Estrutura

```text
sopa-da-vov-
├── README.md
├── pyproject.toml
├── requirements.txt
├── data/
│   └── tasks/
│       ├── sample_tasks.json
│       └── legal_sample_tasks.json
├── examples/
│   └── run_benchmark.py
├── src/
│   └── sopa_da_vovo/
│       ├── __init__.py
│       ├── benchmark.py
│       ├── config.py
│       ├── evaluator.py
│       └── report.py
└── tests/
    └── test_evaluator.py
```

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução rápida

```bash
python examples/run_benchmark.py
```

## O que a base mede

O projeto calcula métricas simples para comparar a resposta gerada com a resposta esperada:
- similaridade textual;
- cobertura de tokens;
- precisão da resposta;
- status final da tarefa (`pass` ou `review`).

## Tarefas de exemplo

O repositório já inclui tarefas básicas e tarefas com contexto jurídico/operacional para servir como ponto de partida.

## Próximos passos recomendados

- adicionar casos mais reais de uso jurídico;
- criar avaliação por categoria;
- exportar relatórios em JSON/CSV;
- comparar diferentes modelos;
- evoluir para benchmark automatizado.

## Status

Estrutura funcional, estável e pronta para evolução.
