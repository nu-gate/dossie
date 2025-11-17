# Dossiê Nubank — guia rápido

- **Fonte do HTML:** `src/index.html`
- **Build:** `python3 minify.py` (gera o `index.html` minificado na raiz)
- **Conteúdo do PDF:** coloque texto em `docs/content.txt` (ou `docs/content_2.txt`) e PDFs em `docs/contents/`
- **Imagens:** `assets/images/`

## Como usar
1. Edite o conteúdo em `src/index.html` (ou cole novos textos/imagens).
2. Rode `python3 minify.py` para embutir imagens críticas em base64 e minificar.
3. Abra `index.html` no navegador ou publique em qualquer host estático.

## Estrutura
```
.
├── assets/              # imagens e recursos
├── docs/                # textos e PDFs de referência
├── ia/                  # docs internas (claude.md, init.md)
├── src/index.html       # fonte legível
├── index.html           # versão minificada final
└── minify.py            # script de build
```
