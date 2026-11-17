# 03 — Mapeamento de ativos

O inventário é a referência comum da equipe. Sem ele, é fácil confundir sistemas, perder contexto ou avaliar algo que não pertence ao escopo.

## Campos recomendados

| Campo | Descrição |
|---|---|
| ID | Identificador interno único, sem dado pessoal. |
| Ativo | Nome lógico fornecido pelo organizador. |
| Tipo | Aplicação, host, serviço, identidade, rede, armazenamento etc. |
| Ambiente | Laboratório, homologação, produção simulada. |
| Proprietário | Equipe ou responsável, quando informado. |
| Criticidade | Baixa, média, alta ou crítica, com justificativa. |
| Escopo | Dentro, fora ou pendente de confirmação. |
| Dependências | Sistemas necessários para seu funcionamento. |
| Dados | Categorias de dados tratados, sem copiar o conteúdo. |
| Controles | Controles esperados ou declarados. |
| Evidência | Referência ao registro associado. |
| Confiança | Alta, média ou baixa, com motivo. |

## Boas práticas

- Use os nomes e identificadores definidos pelo organizador.
- Não invente proprietário, criticidade ou função quando desconhecidos.
- Registre a data em que a informação foi observada.
- Separe fato observado de inferência.
- Atualize o inventário durante o exercício.
- Não cole segredos, tokens ou dados pessoais na planilha.

## Como priorizar ativos

Uma aplicação que trata dados sensíveis e está exposta a usuários externos tende a exigir atenção maior do que um serviço isolado e sem dados críticos. A priorização deve refletir contexto, não apenas o nome do produto ou o número de porta.

Use [modelo de inventário](../templates/inventario-ativos.csv) como ponto de partida.
