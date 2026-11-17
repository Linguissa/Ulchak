# 07 — Revisão de sistemas Windows e Linux

## Objetivo

Revisar a postura de segurança dos sistemas sem transformar a avaliação em uma mudança de configuração não aprovada.

## Windows — áreas de revisão

- versão e estado de suporte;
- atualização e gerenciamento de patches;
- contas locais e grupos administrativos;
- política de autenticação e bloqueio;
- firewall e exposição de serviços;
- proteção de endpoint e configuração antimalware;
- criptografia de disco e proteção de segredos;
- registro de eventos e retenção;
- serviços e tarefas com privilégios elevados;
- políticas de auditoria e controle de aplicações.

## Linux — áreas de revisão

- distribuição, versão e ciclo de suporte;
- atualização de pacotes;
- usuários, grupos e privilégios administrativos;
- permissões de arquivos e diretórios sensíveis;
- serviços habilitados e necessidade operacional;
- firewall e exposição de interfaces;
- configuração de SSH e autenticação;
- mecanismos de controle de acesso;
- logs, sincronização de horário e retenção;
- proteção de chaves e arquivos de configuração.

## Matriz de análise

| Item | Pergunta | Evidência segura |
|---|---|---|
| Atualização | O sistema recebe correções? | Estado de atualização e política vigente, sem expor identificadores sensíveis. |
| Privilégios | O acesso administrativo é restrito? | Relação de papéis revisada e anonimizada. |
| Serviços | Cada serviço tem necessidade e responsável? | Inventário aprovado e justificativa. |
| Firewall | As regras refletem a arquitetura? | Exportação de política com dados sensíveis removidos. |
| Logs | Eventos importantes são registrados? | Configuração de auditoria e exemplo sintético. |
| Segredos | Há armazenamento e rotação adequados? | Evidência de processo; nunca copie o segredo. |
| Recuperação | Existem backups testados? | Registro de teste e resultado, não cópia de dados. |

## Regras de mudança

Uma revisão não autoriza alterar configuração. Mudanças como desabilitar serviços, modificar firewall, bloquear contas, trocar permissões ou instalar agentes exigem autorização específica, janela, plano de reversão e responsável.

## Resultado esperado

Uma lista priorizada de desvios, impacto, evidência, proprietário da correção e forma de reteste. Use a página [Hardening e remediação](13-hardening-e-remediacao.md) para planejar correções.
