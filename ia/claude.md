# Dossiê Investigativo - Nubank

## Visão Geral

Este projeto transforma um dossiê investigativo em PDF sobre o Nubank em uma página HTML interativa e visualmente impactante. O design adota uma estética investigativa/hacker com tema roxo e preto, criando uma atmosfera de revelação clandestina e jornalismo investigativo.

## Objetivo

Apresentar informações críticas sobre o Nubank de forma acessível, organizada e visualmente atraente, facilitando a compreensão de dados complexos por parte do público geral.

## Características do Design

- **Tema Visual**: Roxo e preto com elementos hackers/investigativos
- **Tipografia**: Fontes de fácil leitura, hierarquia clara
- **Navegação**: Sumário clicável para acesso rápido às seções
- **Responsivo**: Funciona em desktop e mobile
- **Acessibilidade**: Alto contraste, estrutura semântica

## Estrutura do Projeto

```
dossie/
├── claude.md           # Este arquivo - documentação
├── index.html          # Página principal do dossiê
├── content.txt         # ADICIONE AQUI: Conteúdo extraído do PDF
└── assets/             # Pasta para imagens e recursos
    └── images/         # Imagens do dossiê
```

## Como Usar

### 1. Adicionar o Conteúdo do PDF

Crie um arquivo `content.txt` na raiz do projeto com todo o conteúdo do PDF:

```bash
# Cole todo o texto do PDF neste arquivo
touch content.txt
```

**IMPORTANTE**: Adicione o caminho do arquivo aqui quando criar:
- **Arquivo de conteúdo**: `[ADICIONE O CAMINHO AQUI]`

### 2. Extrair Imagens do PDF

Se o PDF contiver imagens importantes:

```bash
mkdir -p assets/images
# Extraia as imagens do PDF e coloque em assets/images/
```

### 3. Abrir o Dossiê

Simplesmente abra o arquivo `index.html` em qualquer navegador:

```bash
open index.html  # macOS
xdg-open index.html  # Linux
start index.html  # Windows
```

Ou use um servidor local:

```bash
python -m http.server 8000
# Acesse: http://localhost:8000
```

## Estrutura do HTML

O dossiê está organizado em seções:

1. **Header Impactante**: Título chamativo com subtítulo revelador
2. **Sumário Interativo**: Links para todas as seções
3. **Seções de Conteúdo**:
   - Introdução
   - Contexto
   - Revelações principais
   - Dados e evidências
   - Conclusões
   - Referências
4. **Footer**: Informações adicionais

## Personalização

### Cores

As cores principais podem ser ajustadas no CSS:

```css
--primary: #8b5cf6 (roxo)
--secondary: #6d28d9 (roxo escuro)
--accent: #a78bfa (roxo claro)
--bg-dark: #0a0a0a (preto)
```

### Fontes

O projeto usa:
- **Títulos**: JetBrains Mono (monospace/hacker style)
- **Corpo**: Inter (legibilidade)

### Emojis/Ícones

Emojis são usados estrategicamente para:
- 🔍 Investigação
- ⚠️ Alertas
- 📊 Dados
- 🚨 Urgência
- 💰 Finanças
- 🔒 Segurança

## Tecnologias

- **HTML5**: Estrutura semântica
- **Tailwind CSS**: Estilização via CDN
- **JavaScript Vanilla**: Interatividade mínima
- **CSS Custom**: Animações e tema customizado

## Manutenção

Para atualizar o conteúdo:

1. Edite `content.txt` com o novo texto
2. Atualize as seções relevantes em `index.html`
3. Adicione novas imagens em `assets/images/`
4. Teste a navegação e links do sumário

## Acessibilidade

O dossiê segue práticas de acessibilidade:

- Estrutura semântica HTML5
- Alto contraste de cores
- Textos alternativos para imagens
- Navegação por teclado
- ARIA labels quando necessário

## Considerações Legais

⚠️ **IMPORTANTE**: Este é um documento investigativo/jornalístico. Certifique-se de que:

- Todas as informações são verificáveis
- Fontes são citadas apropriadamente
- Não há difamação ou informações falsas
- O conteúdo está em conformidade com leis de imprensa

## Próximos Passos

1. ✅ Estrutura HTML criada
2. ⏳ Adicionar conteúdo do PDF em `content.txt`
3. ⏳ Extrair e organizar imagens
4. ⏳ Revisar e ajustar formatação
5. ⏳ Testar responsividade
6. ⏳ Validar acessibilidade

## Suporte

Para dúvidas ou melhorias, edite este arquivo ou consulte a documentação do Tailwind CSS: https://tailwindcss.com/docs
