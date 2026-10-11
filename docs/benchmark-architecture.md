# Arquitetura de benchmark sugerida

## 1. Tarefa

Uma tarefa de benchmark legal contém:
- documento de entrada;
- contexto operacional;
- instrução do agente;
- rubrica de avaliação;
- entregável esperado.

## 2. Ambientes de execução

Assim como os benchmarks públicos, a execução deve separar:
- dados do problema;
- ambiente do agente;
- resultados finais;
- avaliação/escore.

A prática recomendada é manter:
- documentos em diretório somente leitura;
- workspace em diretório de execução;
- output em diretório de entrega.

## 3. Métodos de avaliação

Como em benchmarks jurídicos, a avaliação deve considerar:
- completude;
- precisão;
- fonte e evidência;
- clareza e utilizabilidade;
- ausência de erros graves.

## 4. Pipeline recomendado

```text
documentos + tarefa
        ↓
agente / modelo
        ↓
execução com ferramentas e contexto
        ↓
entregável gerado
        ↓
avaliador / rubrica
        ↓
relatório final
```

## 5. Métricas mínimas

- similaridade textual
- cobertura de ideias principais
- precisão da resposta
- status final da tarefa

## 6. Aplicação prática neste repositório

Este repositório implementa uma versão mínima e funcional desse conceito:
- tarefas em JSON;
- avaliação simples por similaridade e cobertura;
- métricas de status;
- estrutura pronta para expandir para workflows jurídicos reais.
