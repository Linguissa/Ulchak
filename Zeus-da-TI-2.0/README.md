# ZEUS DA TI — Red Team Field Manual

<p align="center">
  <strong>Manual de campo para estudo, avaliação autorizada e competições de cibersegurança</strong>
</p>

<p align="center">
  <img alt="Status: documentação educacional" src="https://img.shields.io/badge/status-educacional-2563eb">
  <img alt="Idioma: Português" src="https://img.shields.io/badge/idioma-pt--BR-16a34a">
  <img alt="Foco: Red Team" src="https://img.shields.io/badge/foco-Red%20Team-7c3aed">
  <img alt="Licença: CC BY 4.0" src="https://img.shields.io/badge/licen%C3%A7a-CC%20BY%204.0-lightgrey">
</p>

> **Propósito:** transformar conhecimento de Red Team em um processo claro, reproduzível, ético e tecnicamente defensável. O Zeus prioriza raciocínio, validação segura, documentação e qualidade das evidências — não uma coleção descontextualizada de comandos.

---

## Comece por aqui

| Preciso de… | Abra |
|---|---|
| Entender o método completo | [Metodologia Red Team](docs/02-metodologia-red-team.md) |
| Confirmar o que posso testar | [Regras de engajamento e escopo](docs/01-regras-e-escopo.md) |
| Organizar ativos e serviços | [Mapeamento de ativos](docs/03-mapeamento-de-ativos.md) e [Enumeração](docs/04-enumeracao-e-analise.md) |
| Avaliar aplicações web | [Segurança de aplicações](docs/05-seguranca-web.md) |
| Revisar identidade e Active Directory | [Identidade e diretório](docs/06-identidade-e-active-directory.md) |
| Revisar Windows e Linux | [Revisão de sistemas](docs/07-revisao-de-sistemas.md) |
| Validar uma vulnerabilidade sem causar dano | [Validação segura](docs/08-validacao-de-vulnerabilidades.md) |
| Montar evidências e relatório | [Evidências](docs/09-evidencias.md) e [Relatório](docs/10-relatorio-tecnico.md) |
| Preparar uma competição | [Operação em competição](docs/11-operacao-em-competicao.md) |
| Praticar com cenários controlados | [Laboratório de estudo](docs/12-laboratorio-de-estudo.md) |

## O que mudou nesta edição

- Navegação refeita com caminhos relativos consistentes.
- Conteúdo dividido por objetivo, não apenas por ferramenta.
- Separação explícita entre descoberta, análise, validação, impacto e comunicação.
- Checklists e modelos reutilizáveis para escopo, ativos, achados e evidências.
- Critérios para distinguir fato confirmado, hipótese e falso positivo.
- Orientações para evitar indisponibilidade, exposição de dados e alterações não autorizadas.
- Referências oficiais para aprofundamento e acompanhamento de versões.
- Verificação automática de links e estrutura do repositório via GitHub Actions.

## Princípios do Zeus

1. **Autorização antes da técnica.** Nenhum teste começa sem escopo, permissão e regras claras.
2. **Menor impacto possível.** Preferir observação e verificações não destrutivas; interromper diante de risco inesperado.
3. **Evidência antes de conclusão.** Uma hipótese não é uma vulnerabilidade confirmada.
4. **Reprodutibilidade.** Registrar contexto, horário, ativo, método, resultado e limitações.
5. **Confidencialidade.** Coletar somente o necessário e proteger dados e credenciais.
6. **Correção faz parte do trabalho.** Um achado útil explica como reduzir o risco.
7. **Regulamento oficial prevalece.** Em competição, as regras da edição, do organizador e do avaliador têm prioridade sobre este manual.

## Limites de uso

Este repositório é material educacional. Use-o somente em laboratórios próprios, ambientes de treinamento disponibilizados para esse fim ou avaliações com autorização explícita e escopo documentado. Não use o conteúdo para acessar sistemas de terceiros, coletar credenciais, interromper serviços, contornar controles ou modificar dados sem autorização específica.

O Zeus **não** contém listas de senhas, credenciais, alvos reais, payloads de invasão ou instruções para obter acesso não autorizado. Em exercícios, siga a plataforma e as instruções oficiais do laboratório.

## Estrutura

```text
.
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── docs/
│   ├── 00-visao-geral.md
│   ├── 01-regras-e-escopo.md
│   ├── 02-metodologia-red-team.md
│   ├── 03-mapeamento-de-ativos.md
│   ├── 04-enumeracao-e-analise.md
│   ├── 05-seguranca-web.md
│   ├── 06-identidade-e-active-directory.md
│   ├── 07-revisao-de-sistemas.md
│   ├── 08-validacao-de-vulnerabilidades.md
│   ├── 09-evidencias.md
│   ├── 10-relatorio-tecnico.md
│   ├── 11-operacao-em-competicao.md
│   ├── 12-laboratorio-de-estudo.md
│   ├── 13-hardening-e-remediacao.md
│   ├── 14-glossario.md
│   ├── 15-referencias.md
│   └── 16-alinhamento-worldskills.md
├── examples/
├── templates/
├── scripts/check_repo.py
└── .github/workflows/quality.yml
```

## Qualidade e atualização

A documentação é uma base de estudo, não uma garantia de que um procedimento será aceito em uma prova. Ferramentas, padrões e regulamentos mudam. Confira a versão das referências, o ambiente de laboratório e o regulamento específico antes de cada uso.

Para validar os links e arquivos localmente:

```bash
python scripts/check_repo.py
```

O mesmo teste é executado automaticamente em cada push e pull request.

## Como contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md). Sugestões devem indicar a fonte, a versão, o contexto de teste e os riscos conhecidos. Não envie segredos, dados pessoais, credenciais, alvos reais ou material de terceiros sem permissão.

## Licença

O texto original deste repositório é disponibilizado sob [Creative Commons Attribution 4.0 International](LICENSE). Marcas, logotipos, padrões e materiais de terceiros pertencem aos respectivos titulares e são citados para estudo.
