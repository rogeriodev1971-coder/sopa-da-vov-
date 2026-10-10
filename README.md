# Sopa da Vovó

Projeto base para avaliação de agentes de IA com foco em benchmark, métricas e exemplos práticos.

## Objetivo

Cria uma estrutura simples, reutilizável e fácil de evoluir para:
- benchmark de respostas de IA;
- avaliação de qualidade por tarefa;
- comparação de saídas esperadas vs. geradas;
- organização de experimentos em IA e automação.

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
│       ├── __main__.py
│       ├── benchmark.py
│       ├── cli.py
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

## Execução via CLI

```bash
python -m sopa_da_vovo --tasks data/tasks/sample_tasks.json --output reports/results.json
```

Opcionalmente, você pode comparar respostas vindas de um arquivo JSON:

```bash
python -m sopa_da_vovo \
  --tasks data/tasks/legal_sample_tasks.json \
  --responses data/tasks/responses_demo.json \
  --output reports/legal_results.json
```

## Formato do arquivo de respostas

```json
{
  "legal-001": "O serviço deve ser entregue em até 30 dias após a assinatura. Atrasos superiores a 10 dias geram multa de 2% ao mês.",
  "legal-002": "O cliente deverá enviar a documentação solicitada em até 5 dias úteis após o pedido da prestadora."
}
```

## O que a base mede

O projeto calcula métricas simples para comparar a resposta gerada com a resposta esperada:
- similaridade textual;
- cobertura de tokens;
- precisão da resposta;
- status final da tarefa (`pass` ou `review`).

## Próximos passos recomendados

- adicionar casos reais de uso jurídico;
- criar avaliação por categoria;
- exportar relatórios em JSON/CSV;
- comparar diferentes modelos;
- evoluir para benchmark automatizado.

## Status

Estrutura funcional, estável e pronta para evolução.
