#!/data/data/com.termux/files/usr/bin/bash

# ==========================================
# SCRIPT: releasingsys_file.sh
# DESCRIÇÃO: Commit, push e pré-release completo em um único script
# USO: 
#  updatebot (bash releasingsys_file.sh) "mensagem" "vX.X.X-beta.1" "vX.X.X"
# ==========================================

# 1. Verifica se os argumentos obrigatórios foram passados
if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "❌ Uso: updatebot \"mensagem do commit\" \"vX.X.X-beta.1\" \"VX.X.X.X\""
    echo "   Exemplo: updatebot \"feat: /ajuda\" \"v0.2.0-beta.1\" \"v0.1.4.2\""
    exit 1
fi

# 2. Verifica se o repositório Git existe
if [ ! -d ".git" ]; then
    echo "❌ Este diretório não é um repositório Git."
    exit 1
fi

# 3. Verifica se o GitHub CLI (gh) está instalado e autenticado
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) não encontrado. Instale com: pkg install gh"
    exit 1
fi

# 4. Atribui os argumentos às variáveis
MENSAGEM="$1"
TAG="$2"
TAG_ANTERIOR="$3"

# 5. Exibe o que vai fazer (resumo)
echo "📦 Preparando release:"
echo "   📝 Mensagem: $MENSAGEM"
echo "   🏷️  Tag (Nova): $TAG"
echo "   🏷️  Tag (Anterior): $TAG_ANTERIOR"
echo "=============================="

# 6. Confirma com o usuário (pausa de 5 segundos para cancelar)
echo "⏳ Você tem 10 segundos para cancelar (Ctrl+C) se não quiser prosseguir..."
sleep 10

# 7. Git add, commit e push
echo "⬆️  Adicionando arquivos..."
git add .

echo "📝 Fazendo commit..."
git commit -m "$TAG | $MENSAGEM"

echo "🚀 Enviando para o GitHub..."
git push

# 8. Criação da pré-release com ou sem --notes-start-tag
echo "🏷️  Criando tag e pré-release..."
if [ -n "$TAG_ANTERIOR" ]; then
    # Modo forçado: compara com a tag especificada
    gh release create "$TAG" --prerelease --generate-notes --notes "$MENSAGEM" --notes-start-tag "$TAG_ANTERIOR"
fi

# 9. Mensagem final
echo "✅ Commit, push e pré-release criados com sucesso!"
echo "🔗 Verifique no GitHub: https://github.com/zShelbyTheOne/Omnyrion-Bot-Repo-OFC/releases"