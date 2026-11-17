# 05 — Segurança de aplicações web

Esta página organiza a avaliação de aplicações com base em requisitos e categorias reconhecidos. Para a lista detalhada de casos de teste, consulte o OWASP Web Security Testing Guide (WSTG) e o OWASP Application Security Verification Standard (ASVS).

## 1. Entenda a aplicação

Documente:
- funções de negócio e fluxos principais;
- tipos de usuário e privilégios;
- dados processados e classificados;
- pontos de entrada e integrações;
- operações que alteram estado;
- mecanismos de autenticação, sessão e autorização;
- controles esperados pelo proprietário.

## 2. Áreas de avaliação

| Área | Perguntas de revisão |
|---|---|
| Autenticação | A identidade é verificada de forma consistente? Há proteção adequada para recuperação de conta? |
| Sessão | Ciclo de vida, expiração, revogação e proteção da sessão estão definidos? |
| Autorização | Cada função valida o papel e o contexto do usuário no servidor? |
| Validação de entrada | Dados são validados conforme tipo, formato, tamanho e contexto? |
| Saída | Conteúdo dinâmico é tratado de acordo com o contexto de apresentação? |
| Arquivos | Tipos, tamanho, armazenamento, acesso e retenção são controlados? |
| Erros | Mensagens não revelam segredos, detalhes internos ou dados pessoais? |
| Criptografia | Dados sensíveis usam mecanismos e configurações atuais e adequados? |
| Configuração | Cabeçalhos, CORS, TLS, cookies e configurações de implantação são coerentes? |
| Dependências | Bibliotecas e componentes possuem inventário, atualização e tratamento de vulnerabilidades? |
| Registro | Eventos importantes são registrados sem armazenar segredos? |
| Lógica de negócio | Regras e limites são aplicados no servidor, inclusive em fluxos alternativos? |

## 3. Método seguro de validação

1. Obtenha um usuário de teste e dados sintéticos fornecidos pelo laboratório.
2. Defina qual requisito está sendo avaliado.
3. Observe o comportamento esperado e o comportamento real.
4. Use apenas operações de leitura sempre que possível.
5. Para funções que alteram estado, obtenha autorização específica e use dados descartáveis.
6. Pare quando a evidência mínima estiver estabelecida.
7. Registre a resposta e o contexto sem capturar dados de outros usuários.

Não tente acessar contas de terceiros nem contornar autorização em serviços reais. Em laboratório, siga somente os cenários e limites definidos pelo responsável.

## 4. Como descrever um achado web

- endpoint/função em termos não sensíveis;
- papel de teste utilizado;
- requisito ou controle esperado;
- resultado observado;
- evidência minimizada;
- impacto plausível;
- pré-condições;
- limitações e explicações alternativas;
- correção recomendada.

## 5. Referências principais

- [OWASP WSTG — versão estável 4.2](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP ASVS — versão estável 5.0.0](https://asvs.owasp.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

O WSTG 5.0 está em desenvolvimento; para relatórios reprodutíveis, indique a versão efetivamente consultada. Consulte a página oficial antes de citar identificadores ou requisitos.
