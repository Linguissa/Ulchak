# 13 — Hardening e remediação

Hardening é a redução da superfície de ataque por meio de configurações, processos e controles apropriados. Esta página é voltada à recomendação e à verificação de correções; mudanças reais precisam de aprovação do proprietário.

## Ciclo de correção

1. Confirmar o achado e seu escopo.
2. Identificar proprietário e sistema responsável.
3. Avaliar impacto operacional da mudança.
4. Definir janela, plano de reversão e comunicação.
5. Implementar por processo aprovado.
6. Verificar o estado após a mudança.
7. Retestar o controle relacionado.
8. Registrar resultado e encerrar ou reabrir o achado.

## Controles recorrentes

- atualização e gestão de vulnerabilidades;
- menor privilégio e revisão de acessos;
- autenticação forte para funções sensíveis;
- proteção e rotação de segredos;
- segmentação e exposição mínima de serviços;
- configuração segura de sistemas e aplicações;
- registro e monitoramento de eventos relevantes;
- backup e recuperação testados;
- inventário de ativos e dependências;
- gestão de fornecedores e componentes.

## Plano de remediação

Para cada achado, defina:

| Campo | Conteúdo |
|---|---|
| Ação | Mudança específica recomendada. |
| Responsável | Papel ou equipe responsável. |
| Prioridade | Fundamentada no risco. |
| Dependências | Aprovações, testes, fornecedores ou janelas. |
| Risco de mudança | Possíveis efeitos colaterais. |
| Reversão | Como restaurar o estado anterior. |
| Reteste | Evidência objetiva de correção. |
| Prazo | Data acordada com o proprietário. |

## Cuidado

Não aplique mudanças em sistemas reais apenas porque uma lista de verificação sugere fazê-lo. Mudanças em firewall, contas, permissões, serviços, autenticação ou logs podem causar indisponibilidade. O proprietário deve aprovar e supervisionar a execução.
