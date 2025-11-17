# Pasta de Imagens

## Instruções

Coloque aqui todas as imagens extraídas do PDF do dossiê.

### Como extrair imagens do PDF:

1. **Usando ferramentas online:**
   - PDF.co
   - iLovePDF
   - Smallpdf

2. **Usando software:**
   - Adobe Acrobat
   - GIMP (abre PDFs)
   - Inkscape

3. **Usando linha de comando (Linux/Mac):**
   ```bash
   pdfimages -all seu-dossie.pdf assets/images/imagem
   ```

### Organização:

Nomeie os arquivos de forma descritiva:
- `grafico-receita.png` em vez de `imagem1.png`
- `logo-nubank.jpg` em vez de `img.jpg`
- `tabela-dados.png` em vez de `screenshot.png`

### Formatos suportados:

- JPG/JPEG (fotos, imagens complexas)
- PNG (gráficos, capturas de tela)
- SVG (logos, ícones vetoriais)
- GIF (animações, se necessário)

### Referenciando no HTML:

```html
<img src="assets/images/nome-arquivo.jpg" alt="Descrição da imagem" class="content-image w-full my-6">
```
