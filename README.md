# Sopa da Vovó

Base de benchmark e avaliação para agentes de IA, inspirada em estruturas públicas e abertas de referência do ecossistema Harvey AI.

## Visão geral

Este repositório foi organizado como um ponto de partida para:
- benchmark de agentes de IA;
- tarefas jurídicas e de pesquisa;
- avaliação por rubricas e métricas;
- integração com fluxos de pesquisa profunda e revisão documental.

A abordagem aqui é uma adaptação educacional e prática de projetos públicos relevantes, não uma cópia integral de qualquer repositório terceiro.

## Fontes públicas consideradas

Principais referências públicas e abertas do Harvey AI analisadas para orientar este projeto:

- Harvey LAB — benchmark jurídico para agentes: https://github.com/harveyai/harvey-labs
- BigLaw Bench — benchmark jurídico e avaliação por tarefa: https://github.com/harveyai/biglaw-bench
- Deep Research Starter — workflow de pesquisa aprofundada: https://github.com/harveyai/deep-research-starter
- Harvey org public repos — referências complementares de infraestrutura, extração e integração: https://github.com/harveyai

## O que foi extraído em termos práticos

- organização de tarefas por domínio e área legal;
- separação entre dados de tarefa, execução e avaliação;
- uso de rubricas e critérios de qualidade;
- benchmark orientado para documentos, dados e entregáveis;
- uso de pesquisa profunda para tarefas mais complexas.

## Estrutura do projeto

```text
sopa-da-vov-
├── README.md
├── pyproject.toml
├── requirements.txt
├── data/
│   └── tasks/
│       ├── sample_tasks.json
│       ├── legal_sample_tasks.json
│       └── legal_tasks.json
├── docs/
│   ├── harvey-public-sources.md
│   └── benchmark-architecture.md
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

## Arquitetura de benchmark sugerida

A arquitetura útil para este projeto é:

1. Tarefa
   - instrução
   - documentos
   - contexto
   - rubrica de avaliação

2. Agente
   - prompt do sistema
   - ferramentas e capacidades
   - pipeline de raciocínio

3. Sandbox / ambiente de execução
   - acesso controlado a arquivos
   - documentos somente leitura
   - output e scratch separados

4. Avaliação
   - similaridade textual
   - cobertura de informação
   - precisão e confiabilidade
   - avaliação por rubrica

5. Relatório
   - status da tarefa
   - pontuação por métrica
   - evidências e observações

## Tarefas legais sugeridas

- revisão de cláusulas contratuais;
- resumo executivo de acordos;
- extração de obrigações e prazos;
- análise de risco em documentos;
- revisão de due diligence;
- comparação de termos e estruturas;
- triagem de documentos e evidências.

## Execução

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python examples/run_benchmark.py
```

## Recomendação

Para evoluir de forma legítima e útil:
- usar as estruturas públicas e MIT dos benchmark repos como inspiração;
- manter o código e os dados aceleradores originais fora do projeto;
- priorizar adaptações, documentação e dados próprios;
- diferenciar claramente "referência pública" de "implementação própria".

## Status

Base funcional, com arquitetura inspirada em benchmarks legais públicos e pronta para evolução.
