# 🔍 Dossiê Nubank - Projeto Web

Transformação de dossiê investigativo em PDF para HTML interativo com tema investigativo/hacker.

## 🚀 Início Rápido

1. **Adicione o conteúdo do PDF:**
   ```bash
   # Cole o texto do PDF no arquivo content.txt
   nano content.txt
   ```

2. **Extraia as imagens do PDF:**
   ```bash
   # Salve as imagens em assets/images/
   # Exemplo: assets/images/grafico1.png
   ```

3. **Edite o HTML:**
   - Abra `index.html`
   - Substitua todos os `[ADICIONE...]` pelo conteúdo de `content.txt`
   - Adicione as referências de imagens onde indicado

4. **Visualize o resultado:**
   ```bash
   # Opção 1: Abra diretamente no navegador
   open index.html

   # Opção 2: Use um servidor local
   python3 -m http.server 8000
   # Acesse: http://localhost:8000
   ```

## 📁 Estrutura do Projeto

```
dossie/
├── claude.md              # Documentação completa do projeto
├── README.md              # Este arquivo
├── index.html             # Página principal do dossiê
├── content.txt            # Cole aqui o conteúdo do PDF
├── .gitignore             # Arquivos ignorados pelo Git
└── assets/
    └── images/            # Imagens do dossiê
        └── README.md      # Instruções para imagens
```

## 🎨 Características

- ✅ Tema roxo/preto investigativo estilo hacker
- ✅ Design responsivo (mobile + desktop)
- ✅ Sumário interativo com navegação suave
- ✅ Animações e efeitos cyberpunk
- ✅ Seções bem organizadas
- ✅ Fácil de personalizar
- ✅ Sem dependências externas (usa CDN do Tailwind)

## 📝 Próximos Passos

- [ ] Adicionar conteúdo do PDF em `content.txt`
- [ ] Extrair imagens do PDF
- [ ] Preencher todas as seções do `index.html`
- [ ] Revisar e ajustar formatação
- [ ] Testar em diferentes navegadores
- [ ] Publicar (GitHub Pages, Netlify, etc.)

## 🔧 Personalização

### Mudar cores:
Edite as variáveis CSS no `<style>` do `index.html`:
```css
--primary: #8b5cf6;      /* roxo principal */
--secondary: #6d28d9;    /* roxo escuro */
--accent: #a78bfa;       /* roxo claro */
```

### Adicionar seções:
Copie uma seção existente e modifique:
```html
<section id="nova-secao" class="section mb-20">
    <div class="neon-border rounded-lg p-8 bg-black/50">
        <h2 class="text-4xl font-bold mb-6 text-purple-400">
            🎯 NOVA SEÇÃO
        </h2>
        <!-- Conteúdo aqui -->
    </div>
</section>
```

## 📖 Documentação Completa

Consulte `claude.md` para documentação detalhada sobre:
- Como usar o projeto
- Estrutura do HTML
- Personalização avançada
- Acessibilidade
- Considerações legais

## ⚖️ Aviso Legal

Este é um documento investigativo/jornalístico. Certifique-se de que todas as informações são verificáveis e estão em conformidade com as leis aplicáveis.

## 🤝 Contribuições

Este é um projeto pessoal. Personalize conforme suas necessidades.

---

**Versão:** 1.0
**Última atualização:** 2025-11-15
