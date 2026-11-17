#!/usr/bin/env python3
"""Valida a estrutura e os links Markdown internos do Zeus.

Usa somente a biblioteca padrão do Python. Não acessa a rede.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE",
    "docs/00-visao-geral.md", "docs/01-regras-e-escopo.md",
    "docs/02-metodologia-red-team.md", "docs/03-mapeamento-de-ativos.md",
    "docs/04-enumeracao-e-analise.md", "docs/05-seguranca-web.md",
    "docs/06-identidade-e-active-directory.md", "docs/07-revisao-de-sistemas.md",
    "docs/08-validacao-de-vulnerabilidades.md", "docs/09-evidencias.md",
    "docs/10-relatorio-tecnico.md", "docs/11-operacao-em-competicao.md",
    "docs/12-laboratorio-de-estudo.md", "docs/13-hardening-e-remediacao.md",
    "docs/14-glossario.md", "docs/15-referencias.md",
    "docs/16-alinhamento-worldskills.md", "scripts/check_repo.py",
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
errors = []

for item in REQUIRED:
    if not (ROOT / item).is_file():
        errors.append(f"Arquivo obrigatório ausente: {item}")

for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    try:
        content = md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"Codificação inválida: {md.relative_to(ROOT)}")
        continue
    for target in LINK_RE.findall(content):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("/"):
            errors.append(f"Link absoluto não permitido em {md.relative_to(ROOT)}: {target}")
            continue
        path = (md.parent / target).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Link sai do repositório em {md.relative_to(ROOT)}: {target}")
            continue
        if not path.exists():
            errors.append(f"Link quebrado em {md.relative_to(ROOT)}: {target}")

if errors:
    print("FALHA — verificação do Zeus encontrou problemas:")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)

print("OK — estrutura obrigatória e links Markdown internos válidos.")
print(f"Arquivos Markdown verificados: {len(list(ROOT.rglob('*.md')))}")
