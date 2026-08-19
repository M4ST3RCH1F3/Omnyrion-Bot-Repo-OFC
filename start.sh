#!/data/data/com.termux/files/usr/bin/bash

# ==============================================
# 1. DESCOBRE ONDE ESTE SCRIPT ESTÁ (A RAIZ DO BOT)
# ==============================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

echo "📂 Diretório do bot: $SCRIPT_DIR"

# ==============================================
# 2. VERIFICA E INSTALA AS DEPENDÊNCIAS (requirements.txt)
# ==============================================
echo "📦 Verificando dependências..."

# Garante que o pip está instalado
if ! command -v pip &> /dev/null; then
    echo "⚠️ Pip não encontrado. Instalando pip..."
    python -m ensurepip --upgrade || pkg install python-pip -y
fi

# Se existir o requirements.txt, instala tudo
if [ -f "requirements.txt" ]; then
    echo "📄 requirements.txt encontrado. Instalando/atualizando bibliotecas..."
    pip install -r requirements.txt --quiet --upgrade
    echo "✅ Dependências verificadas."
else
    echo "⚠️  Arquivo requirements.txt não encontrado. Pulando instalação."
fi

echo "=============================="

# ==============================================
# 3. VERIFICA SE O TMUX ESTÁ INSTALADO
# ==============================================
if ! command -v tmux &> /dev/null; then
    echo "❌ Tmux não encontrado. Instale com: pkg install tmux -y"
    exit 1
fi

# ==============================================
# 4. EVITA DUPLICAR A SESSÃO DO BOT
# ==============================================
if tmux has-session -t omnyrion 2>/dev/null; then
    echo "⚠️  O bot JÁ ESTÁ RODANDO na sessão 'omnyrion'."
    echo "   Para ver os logs: tmux attach -t omnyrion"
    echo "   Para sair dos logs sem matar: Ctrl+B, D"
    exit 0
fi

# ==============================================
# 5. INICIA O BOT EM SEGUNDO PLANO (background)
# ==============================================
tmux new-session -d -s omnyrion "python src/main.py"

# ==============================================
# 6. CONFIRMAÇÃO FINAL
# ==============================================
echo "✅ Bot iniciado com sucesso na sessão 'omnyrion'."
echo "   Para ver o log: tmux attach -t omnyrion"