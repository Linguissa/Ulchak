# 08 — Validação de vulnerabilidades

## O princípio central

O objetivo é determinar se uma condição insegura existe e qual risco representa, usando o menor nível de impacto necessário. Não é preciso causar dano para demonstrar um problema.

## Escala de evidência

1. **Indício:** alerta, banner ou configuração suspeita.
2. **Corroboração:** segunda fonte independente confirma a condição.
3. **Validação controlada:** comportamento confirma a falha em dados sintéticos ou laboratório autorizado.
4. **Impacto demonstrado:** consequência limitada foi comprovada, dentro do escopo e com autorização.

Não descreva um indício como exploração confirmada.

## Procedimento de decisão

- O ativo está explicitamente no escopo?
- Existe autorização para o tipo de validação proposto?
- Há risco de indisponibilidade, alteração ou exposição de dados?
- É possível obter a mesma evidência por configuração, documentação ou observação não destrutiva?
- O ambiente contém dados sintéticos e mecanismo de recuperação?
- O responsável sabe como a atividade será interrompida?

Se uma resposta crítica estiver ausente, não execute o teste. Solicite orientação.

## Falso positivo e falso negativo

- **Falso positivo:** o alerta indica problema, mas a condição não se aplica ou não possui impacto confirmado.
- **Falso negativo:** o teste não encontra o problema, embora ele possa existir em outras condições.

Registre limitações de cobertura, autenticação, versão, configuração e tempo disponível.

## Severidade

Considere:
- impacto sobre confidencialidade, integridade e disponibilidade;
- alcance e criticidade do ativo;
- pré-condições e privilégios exigidos;
- exposição e frequência plausível;
- controles compensatórios;
- confiabilidade da evidência.

Use CVSS como linguagem técnica padronizada quando apropriado, mas não trate a pontuação como substituta do contexto de negócio. Registre a versão e o vetor usados. A referência atual é [FIRST CVSS](https://www.first.org/cvss/).

## Quando parar

Pare quando a evidência mínima estiver estabelecida, quando houver risco não previsto, quando o ativo sair do escopo ou quando o responsável solicitar. Nunca continue apenas para aumentar a severidade aparente.
