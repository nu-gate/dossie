#!/usr/bin/env python3
"""
Minify src/index.html (fonte) e gera index.html otimizado na raiz.
Inclui imagens críticas inline em base64 e remove espaços/comentários para reduzir o tamanho.
"""

from pathlib import Path
import base64
import re

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "index.html"
OUT = ROOT / "index.html"

# Mapeie apenas as imagens realmente usadas que valem ser embutidas
EMBED_IMAGES = {
    "assets/images/logo.png": "image/png",
    "assets/images/intro.webp": "image/webp",
    "assets/images/david_velez..jpeg": "image/jpeg",
    "assets/images/founders.jpg": "image/jpeg",
    "assets/images/cards.png": "image/png",
    "assets/images/ipo.jpeg": "image/jpeg",
}

def read_src() -> str:
    if not SRC.exists():
        raise FileNotFoundError(f"Arquivo fonte não encontrado: {SRC}")
    return SRC.read_text(encoding="utf-8")

def embed_images(html: str) -> str:
    for rel_path, mime_type in EMBED_IMAGES.items():
        img_path = ROOT / rel_path
        if not img_path.exists():
            print(f"Warning: {rel_path} not found; skipping embed.")
            continue
        data = base64.b64encode(img_path.read_bytes()).decode("utf-8")
        data_uri = f"data:{mime_type};base64,{data}"
        html = html.replace(f'src="{rel_path}"', f'src="{data_uri}"')
    return html

def minify_html(html: str) -> str:
    # Remove comentários (exceto condicionais IE)
    html = re.sub(r"<!--(?!\[if).*?-->", "", html, flags=re.DOTALL)
    # Colapsa espaços
    html = re.sub(r"\s+", " ", html)
    # Remove espaços entre tags
    html = re.sub(r">\s+<", "><", html)
    # Ajusta espaços imediatos
    html = re.sub(r">\s+", ">", html)
    html = re.sub(r"\s+<", "<", html)
    return html.strip()

def main() -> None:
    html = read_src()
    html = embed_images(html)
    html = minify_html(html)
    OUT.write_text(html, encoding="utf-8")
    print(f"Minified HTML created: {OUT}")
    print(f"Output size: {OUT.stat().st_size} bytes")

if __name__ == "__main__":
    main()
