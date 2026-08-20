#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# SCRIPT: releasingsys_file.sh
# DESCRIÇÃO: Commit, push e release interativo com entrada multilinha
# USO: 
#   Basta executar: repoupdate
#   Para escrever a mensagem com várias linhas, pressione Enter para quebrar.
#   Para finalizar a mensagem, pressione Ctrl+D (Volume - + D).
# ==========================================

# 1. MENSAGEM DO COMMIT (com entrada multilinha)
echo ""
echo "📝 Digite a mensagem do commit (Enter para quebrar linha, Ctrl+D para finalizar):"
MENSAGEM=$(cat)

if [ -z "$MENSAGEM" ]; then
    echo "❌ Mensagem vazia. Operação cancelada."
    exit 1
fi

# 2. TAG NOVA
echo ""
echo "🏷️  Digite o nome da tag (nova):"
echo "   Exemplo: v0.2.0"
read -r TAG
if [ -z "$TAG" ]; then
    echo "❌ Tag vazia. Operação cancelada."
    exit 1
fi

# 3. TAG ANTERIOR
echo ""
echo "🏷️  Digite o nome da tag anterior (para comparação):"
echo "   Exemplo: v0.1.4.2"
read -r TAG_ANTERIOR
if [ -z "$TAG_ANTERIOR" ]; then
    echo "❌ Tag anterior vazia. Operação cancelada."
    exit 1
fi

# 4. TIPO DE RELEASE
echo ""
echo "📂 Escolha o tipo de release:"
echo "  1) Estável (release)"
echo "  2) Pré-release (beta/alpha/rc)"
echo -n "Digite o número (1 ou 2): "
read -r opcao

case $opcao in
    1) TIPO="stable"; FLAG_PRERELEASE="" ;;
    2) TIPO="pre"; FLAG_PRERELEASE="--prerelease" ;;
    *) TIPO="stable"; FLAG_PRERELEASE="" ;;
esac

# 5. RESUMO E CONFIRMAÇÃO
echo ""
echo "📦 Resumo da release:"
echo "   📝 Mensagem:"
echo "   -----------------------------"
echo "$MENSAGEM"
echo "   -----------------------------"
echo "   🏷️  Tag (Nova): $TAG"
echo "   🏷️  Tag (Anterior): $TAG_ANTERIOR"
echo "   📂 Tipo: $TIPO"
echo ""
echo -n "Tudo correto? (s/N): "
read -r confirmacao
if [[ "$confirmacao" != "s" && "$confirmacao" != "S" ]]; then
    echo "❌ Operação cancelada."
    exit 0
fi

# 6. VERIFICA DEPENDÊNCIAS
if [ ! -d ".git" ]; then
    echo "❌ Este diretório não é um repositório Git."
    exit 1
fi

if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) não encontrado. Instale com: pkg install gh"
    exit 1
fi

# 7. GIT ADD, COMMIT E PUSH
echo ""
echo "⬆️  Adicionando arquivos..."
git add .

echo "📝 Fazendo commit..."
git commit -m "$TAG | $MENSAGEM"

echo "🚀 Enviando para o GitHub..."
git pull --rebase origin main
git push

# 8. CRIAÇÃO DA RELEASE
echo "🏷️  Criando tag e release $TIPO..."
gh release create "$TAG" $FLAG_PRERELEASE --generate-notes --notes "$MENSAGEM"

# 9. MENSAGEM FINAL
echo ""
echo "✅ Commit, push e release criados com sucesso!"
echo "🔗 Verifique no GitHub: https://github.com/zShelbyTheOne/Omnyrion-Bot-Repo-OFC/releases"