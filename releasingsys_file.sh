#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# SCRIPT: releasingsys_file.sh
# DESCRIÇÃO: Commit, push e release com menu interativo
# USO: 
#   Basta executar: repoupdate
#   O script vai perguntar tudo passo a passo.
# ==========================================

# 1. Função para perguntar o tipo de release
escolher_tipo() {
    echo ""
    echo "📂 Escolha o tipo de release:"
    echo "  1) Estável (release)"
    echo "  2) Pré-release (beta/alpha/rc)"
    echo -n "Digite o número (1 ou 2): "
    read -r opcao
    case $opcao in
        1) echo "stable" ;;
        2) echo "pre" ;;
        *) echo "stable" ;;  # padrão
    esac
}

# 2. Pergunta a mensagem do commit
echo ""
echo "📝 Digite a mensagem do commit:"
read -r MENSAGEM

# 3. Pergunta a tag nova
echo ""
echo "🏷️  Digite o nome da tag (nova):"
echo "   Exemplo: v0.2.0"
read -r TAG

# 4. Pergunta a tag anterior
echo ""
echo "🏷️  Digite o nome da tag anterior (para comparação):"
echo "   Exemplo: v0.1.4.2"
read -r TAG_ANTERIOR

# 5. Pergunta o tipo de release
TIPO=$(escolher_tipo)

# 6. Monta a flag do gh
if [ "$TIPO" == "pre" ]; then
    FLAG_PRERELEASE="--prerelease"
else
    FLAG_PRERELEASE=""
fi

# 7. Resumo
echo ""
echo "📦 Preparando release:"
echo "   📝 Mensagem: $MENSAGEM"
echo "   🏷️  Tag (Nova): $TAG"
echo "   🏷️  Tag (Anterior): $TAG_ANTERIOR"
echo "   📂 Tipo: $TIPO"
echo "=============================="

# 8. Confirmação (10 segundos)
echo "⏳ Você tem 10 segundos para cancelar (Ctrl+C) se não quiser prosseguir..."
sleep 10

# 9. Verifica se está em um repositório Git
if [ ! -d ".git" ]; then
    echo "❌ Este diretório não é um repositório Git."
    exit 1
fi

# 10. Verifica se o GitHub CLI está instalado
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) não encontrado. Instale com: pkg install gh"
    exit 1
fi

# 11. Git add, commit e push
echo ""
echo "⬆️  Adicionando arquivos..."
git add .

echo "📝 Fazendo commit..."
git commit -m "$TAG | $MENSAGEM"

echo "🚀 Enviando para o GitHub..."
git pull --rebase origin main
git push

# 12. Criação da release
echo "🏷️  Criando tag e release $TIPO..."
gh release create "$TAG" $FLAG_PRERELEASE --generate-notes --notes "$MENSAGEM"

# 13. Mensagem final
echo ""
echo "✅ Commit, push e release criados com sucesso!"
echo "🔗 Verifique no GitHub: https://github.com/zShelbyTheOne/Omnyrion-Bot-Repo-OFC/releases"