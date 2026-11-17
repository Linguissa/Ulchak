# 02 — Metodologia Red Team

Esta página fornece um fluxo repetível de avaliação. O nível de profundidade depende do objetivo, do tempo, do risco e do regulamento.

## Fase A — Preparação

**Entrada:** autorização, objetivo e regulamento.

**Atividades:**
- transformar o objetivo em perguntas verificáveis;
- registrar escopo positivo e negativo;
- identificar dependências críticas e janelas;
- definir contatos, critérios de parada e tratamento de dados;
- preparar modelos de inventário e evidências.

**Saída:** plano aprovado e rastreável.

## Fase B — Contextualização e descoberta

Entenda a arquitetura e os ativos autorizados antes de formular conclusões. Registre a origem de cada observação, a data e o grau de confiança. Diferencie dados fornecidos pelo organizador, informações públicas e resultados observados no laboratório.

**Perguntas úteis:**
- Qual é o objetivo de negócio ou de competição?
- Quais ativos suportam esse objetivo?
- Quais identidades e papéis existem?
- Quais dados são sensíveis?
- Quais controles deveriam proteger cada componente?

**Saída:** inventário inicial, mapa de dependências e hipóteses priorizadas.

## Fase C — Enumeração e análise

Faça observações proporcionais ao escopo e à criticidade. A enumeração deve responder a uma pergunta: “Que informação necessária ainda falta para avaliar este controle?”

Para cada observação, registre:
- ativo e componente;
- método e versão da ferramenta, se aplicável;
- data/hora e origem;
- resultado literal ou referência à evidência;
- interpretação;
- limitações e grau de confiança.

Não confunda um banner, uma versão declarada ou um resultado automatizado com prova de vulnerabilidade.

## Fase D — Formação e priorização de hipóteses

Uma hipótese deve conter: condição observada, controle esperado, possível falha, impacto plausível e forma segura de validação.

Priorize por:
- criticidade do ativo;
- sensibilidade dos dados;
- exposição e acessibilidade;
- facilidade de ocorrência;
- impacto sobre confidencialidade, integridade e disponibilidade;
- confiança da evidência.

## Fase E — Validação controlada

- use primeiro evidência de configuração e comportamento não destrutivo;
- prefira uma demonstração mínima e reversível em laboratório;
- não extraia dados reais além do mínimo necessário;
- não altere estado, permissões ou disponibilidade sem autorização específica;
- não prossiga quando a evidência já for suficiente.

**Regra:** o objetivo é provar o risco, não maximizar o acesso.

## Fase F — Análise de impacto

Explique o que um agente poderia conseguir em termos de negócio, sem exagerar. Identifique pré-condições, barreiras, alcance, ativos afetados e controles que poderiam detectar ou limitar o evento.

## Fase G — Comunicação e correção

Cada achado deve apresentar resumo, evidência, contexto, impacto, severidade justificada, limitações, recomendação e referência. A equipe responsável deve conseguir entender e corrigir o problema sem depender de uma conversa informal.

## Fase H — Reteste e encerramento

Confirme a correção usando a mesma condição de teste, no mesmo escopo e com evidência comparável. Registre o resultado como corrigido, parcialmente corrigido, não corrigido ou não retestado.

## Fluxo rápido

```text
AUTORIZAÇÃO
    ↓
ESCOPO E REGRAS
    ↓
MAPEAMENTO DO AMBIENTE
    ↓
ENUMERAÇÃO E ANÁLISE
    ↓
HIPÓTESE PRIORIZADA
    ↓
VALIDAÇÃO NÃO DESTRUTIVA
    ↓
EVIDÊNCIA + IMPACTO
    ↓
RELATÓRIO + REMEDIAÇÃO
    ↓
RETESTE + ENCERRAMENTO
```
