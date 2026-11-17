# 10 — Relatório técnico

## Estrutura sugerida

1. **Capa e controle:** nome do exercício, versão, datas, classificação e responsáveis.
2. **Resumo executivo:** objetivo, escopo, principais conclusões e riscos prioritários.
3. **Escopo e limitações:** ativos incluídos, exclusões, janelas e restrições.
4. **Metodologia:** fases realizadas, padrões e versões consultadas.
5. **Visão geral:** áreas avaliadas e cobertura alcançada.
6. **Achados:** um registro padronizado para cada problema confirmado.
7. **Recomendações:** ações específicas, prioridade, responsável sugerido e prazo orientativo.
8. **Reteste:** estado de cada correção.
9. **Apêndices:** inventário minimizado, glossário e referências.

## Modelo de achado

### [ID] Título claro e específico

- **Severidade:** crítica / alta / média / baixa / informativa.
- **Confiança:** alta / média / baixa.
- **Ativo:** identificador autorizado e não sensível.
- **Resumo:** o que foi observado.
- **Condição:** requisito ou controle que não foi atendido.
- **Evidência:** referência a material minimizado.
- **Impacto:** consequência plausível, com contexto.
- **Pré-condições:** condições necessárias para a ocorrência.
- **Limitações:** o que não foi testado ou não pôde ser confirmado.
- **Recomendação:** correção técnica e/ou processual.
- **Reteste:** critério objetivo de sucesso.

## Linguagem precisa

Prefira:
- “Foi observada a configuração X no ativo Y, o que pode permitir Z sob as condições descritas.”
- “O alerta não foi confirmado por teste controlado; permanece como hipótese.”
- “O impacto foi limitado a dados sintéticos no ambiente de laboratório.”

Evite:
- “O sistema inteiro está comprometido” sem evidência;
- “Crítico” sem justificar impacto e contexto;
- “Explorável” quando há apenas uma versão potencialmente afetada;
- conclusões absolutas baseadas em cobertura parcial.

## Priorização de correções

Recomende primeiro as correções que reduzem exposição significativa, eliminam privilégio excessivo, protegem dados sensíveis e melhoram detecção. Para cada ação, indique responsável, dependências e forma de verificar o resultado.

Use o [modelo de relatório](../templates/relatorio-tecnico.md) e o [modelo de achado](../templates/achado.md).
