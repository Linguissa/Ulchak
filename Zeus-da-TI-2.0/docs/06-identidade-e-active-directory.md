# 06 — Identidade e Active Directory

## Objetivo

Avaliar se identidades, grupos, privilégios e políticas de autenticação estão coerentes com o princípio do menor privilégio e com as necessidades do ambiente.

## Modelo mental

- **Identidade:** quem ou o que está solicitando acesso.
- **Autenticação:** como a identidade é verificada.
- **Autorização:** quais ações a identidade pode executar.
- **Privilégio:** nível de capacidade concedida.
- **Sessão:** contexto de acesso mantido após a autenticação.
- **Diretório:** serviço que organiza identidades, grupos, dispositivos e políticas.

## Áreas de revisão

### Contas e ciclo de vida

Verifique se existem processos para criação, alteração, revisão periódica, bloqueio e remoção de contas. Contas inativas, órfãs ou sem proprietário definido precisam de análise.

### Grupos e privilégios

Revise associação a grupos privilegiados, delegações, permissões herdadas e contas de serviço. A justificativa deve existir e ser compatível com a função.

### Autenticação

Analise política de senha, autenticação multifator quando aplicável, mecanismos legados, proteção contra tentativas indevidas e processos de recuperação.

### Contas de serviço

Verifique proprietário, finalidade, privilégio mínimo, rotação/gestão de segredos, dependências e monitoramento. Segredos não devem aparecer em documentos ou evidências.

### Políticas e configuração

Revise políticas efetivamente aplicadas, diferenças entre unidades organizacionais, exceções e dispositivos fora de conformidade.

### Auditoria

Confirme se eventos de autenticação, alteração de privilégio, criação de conta e mudanças de política são registrados, protegidos e monitorados.

## Sinais de risco para investigar

- privilégios sem justificativa;
- contas sem proprietário ou sem uso há longo período;
- exceções permanentes a políticas;
- autenticação fraca em funções sensíveis;
- segredos compartilhados ou sem ciclo de rotação;
- ausência de revisão de acesso;
- trilhas de auditoria insuficientes;
- dependências entre contas de serviço e sistemas críticos não documentadas.

Esses sinais não confirmam, isoladamente, uma vulnerabilidade explorável. São itens de revisão que precisam de contexto e evidência.

## Evidências recomendadas

Use exportações autorizadas e minimizadas de configuração, identificação de política, data da coleta, escopo da consulta e justificativa do risco. Mascare nomes pessoais e identificadores sempre que possível.

## Remediação típica

Aplicar menor privilégio, retirar permissões obsoletas, estabelecer proprietário para contas de serviço, revisar autenticação, proteger segredos, monitorar mudanças críticas e testar o processo de revogação.

Não tente obter credenciais, reutilizar senhas ou alterar relações de confiança. Qualquer validação que modifique identidade ou privilégio exige autorização expressa e ambiente controlado.
