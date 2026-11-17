# 01 — Regras de engajamento e escopo

**Nenhum teste começa sem autorização explícita.** Em competições, a autorização é a fornecida pelo organizador e limitada ao ambiente, horário e ações definidos por ele.

## 1. Elementos que precisam estar definidos

| Elemento | Pergunta que precisa ser respondida |
|---|---|
| Autoridade | Quem autorizou a avaliação e com qual legitimidade? |
| Objetivo | O que deve ser avaliado ou demonstrado? |
| Ativos permitidos | Quais sistemas, aplicações, contas e redes fazem parte do exercício? |
| Exclusões | O que não pode ser tocado? |
| Janela | Quando a atividade pode ocorrer? |
| Técnicas permitidas | Quais categorias de teste estão autorizadas? |
| Técnicas proibidas | O que é expressamente vedado? |
| Limites de impacto | Quais níveis de carga, alteração e acesso são aceitáveis? |
| Dados | Como tratar dados pessoais, credenciais e informações confidenciais? |
| Contatos | Quem deve ser avisado em caso de falha ou incidente? |
| Parada | Qual evento obriga interromper os testes? |
| Retenção | Onde e por quanto tempo as evidências podem ser guardadas? |

## 2. Escopo positivo e negativo

- **Escopo positivo:** ativos e ações expressamente permitidos.
- **Escopo negativo:** ativos, dados e ações excluídos.
- **Escopo ambíguo:** qualquer item não descrito com clareza. Trate como não autorizado até receber confirmação escrita.

Não presuma que um endereço, subdomínio, conta relacionada ou serviço de terceiro está autorizado por estar próximo do alvo principal.

## 3. Critérios de interrupção

Interrompa imediatamente e comunique o responsável quando:

- um serviço apresentar instabilidade inesperada;
- houver risco de perda, alteração ou exposição de dados;
- o teste alcançar um ativo fora do escopo;
- aparecer informação pessoal ou segredo que não seja necessário para a avaliação;
- a autorização ou a janela de teste deixar de ser válida;
- os resultados divergirem significativamente do comportamento esperado;
- o organizador, responsável ou avaliador solicitar a parada.

## 4. Registro mínimo

Antes de iniciar, salve a autorização, versão do regulamento, horário, escopo, exclusões, contatos e critérios de parada. Use o arquivo [modelo de escopo](../templates/escopo-e-regras.md).

## 5. Em caso de dúvida

Não “teste para descobrir”. Pergunte ao responsável e aguarde uma definição. A ausência de proibição explícita não equivale a autorização.
