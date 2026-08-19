#!/data/data/com.termux/files/usr/bin/bash

# 1. Descobre onde este script está (a raiz do projeto)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 2. Caminhos
MODELO="$SCRIPT_DIR/bashrc_model"
DESTINO="$HOME/.bashrc"

# 3. Verifica se o modelo existe
if [ ! -f "$MODELO" ]; then
    echo "❌ Arquivo bashrc_model não encontrado."
    echo "   Crie ele com: cp ~/.bashrc \"$SCRIPT_DIR/bashrc_model\""
    exit 1
fi

# 4. Faz um backup do .bashrc atual (se existir)
if [ -f "$DESTINO" ]; then
    echo "📦 Fazendo backup do .bashrc atual..."
    cp "$DESTINO" "$DESTINO.backup_$(date +%Y%m%d_%H%M%S)"
    echo "✅ Backup criado em: $DESTINO.backup_*"
fi

# 5. Copia o modelo para o destino
cp "$MODELO" "$DESTINO"
echo "✅ .bashrc atualizado com sucesso!"

# 6. Opcional: recarregar o .bashrc na sessão atual
echo "🔄 Para recarregar na sessão atual, rode: source ~/.bashrc"
