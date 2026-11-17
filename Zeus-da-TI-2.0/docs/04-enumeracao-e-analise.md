# 04 — Enumeração e análise

## Objetivo

Construir uma visão confiável do ambiente autorizado: componentes, funções, dependências, versões declaradas, controles e lacunas de informação.

## Princípios

1. Comece pelos dados entregues pelo organizador e pela documentação do ambiente.
2. Confirme o escopo antes de qualquer observação técnica.
3. Prefira inventário e consultas de leitura a testes que alterem estado.
4. Registre a origem e a data de cada informação.
5. Não trate detecção automatizada como confirmação final.

## Categorias para organizar observações

### Rede e serviços

Registre a finalidade aparente do serviço, ativo associado, exposição definida pelo laboratório, responsável, dependências e necessidade de acesso. Um número de porta isolado não identifica com certeza um produto nem sua versão.

### Sistemas operacionais

Registre família, versão declarada, ciclo de suporte conhecido, política de atualização e controles de segurança observáveis. Verifique a informação por fontes independentes quando a decisão depender dela.

### Aplicações

Mapeie páginas e funções fornecidas no exercício, tipos de usuário, fluxos de autenticação, operações sensíveis e integrações. Não envie dados de teste a funções que possam afetar pessoas ou sistemas reais.

### Identidade

Identifique os tipos de conta, papéis, grupos, mecanismos de autenticação, processos de concessão e revogação e dependências de serviço.

### Dados e armazenamento

Classifique os tipos de dados, locais de armazenamento, retenção e controles de acesso. Não copie conteúdo sensível para provar que ele existe; registre apenas metadados mínimos autorizados.

## Ficha de observação

Para cada item, responda:

- O que foi observado literalmente?
- Em qual ativo e momento?
- Qual é a fonte da informação?
- O que isso sugere?
- Quais outras explicações são possíveis?
- O que falta para confirmar?
- Qual é o menor teste permitido que resolveria a dúvida?

## Falsos positivos comuns

- versão declarada diferente da versão efetivamente instalada;
- serviço identificado incorretamente por banner genérico;
- vulnerabilidade aplicável a outro sistema operacional ou configuração;
- achado que depende de um recurso desabilitado;
- alerta sem impacto demonstrado;
- exposição pública que não contém informação sensível nem permite ação relevante.

## Saída esperada

Inventário atualizado, mapa de dependências, lista de hipóteses priorizadas e lacunas registradas. Não é necessário testar tudo: priorize o que responde ao objetivo do exercício.
