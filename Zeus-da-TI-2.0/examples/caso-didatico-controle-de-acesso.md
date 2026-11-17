# Exemplo didático — controle de acesso em aplicação fictícia

> Todos os nomes, papéis e resultados desta página são inventados. O exemplo não descreve um alvo real nem um procedimento de intrusão.

## Contexto

Uma aplicação de laboratório oferece dois papéis: `Leitor` e `Gestor`. O instrutor fornece uma matriz de permissões e uma captura simulada de configuração.

## Observação

A matriz informa que a função “Exportar relatório de administração” deveria estar disponível somente para `Gestor`. A configuração fictícia fornecida indica que ambos os papéis receberam a permissão.

## Análise

- **Fato:** a matriz e a configuração de demonstração são divergentes.
- **Hipótese:** usuários com papel `Leitor` podem visualizar uma função administrativa.
- **Ainda não demonstrado:** se a aplicação aplica a permissão corretamente no servidor.
- **Validação segura:** o instrutor pode fornecer um resultado sintético de teste de autorização, sem dados reais e sem modificar o estado do sistema.

## Achado demonstrativo

**Título:** Permissão administrativa atribuída a papel de leitura.

**Impacto potencial:** exposição de relatórios administrativos a usuários que não deveriam acessá-los. O impacto depende do conteúdo do relatório e da aplicação real da regra no servidor.

**Recomendação:** aplicar autorização no servidor com negação por padrão, centralizar a política de papéis e adicionar testes automatizados para cada função sensível.

**Reteste:** demonstrar que o papel `Leitor` recebe uma resposta de acesso negado à função e que o papel `Gestor` mantém o acesso legítimo, usando exclusivamente contas e dados sintéticos do laboratório.
