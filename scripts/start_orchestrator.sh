#!/bin/bash

# Script de inicialização do Autonomous Orchestrator
# Uso: chmod +x scripts/start_orchestrator.sh && ./scripts/start_orchestrator.sh

echo "=========================================================="
echo "🚀 INICIANDO AUTONOMOUS ORCHESTRATOR"
echo "=========================================================="
echo ""

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3."
    exit 1
fi

# Verificar se o pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale pip3."
    exit 1
fi

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install -r requirements.txt

# Carregar variáveis de ambiente
if [ -f .env ]; then
    echo "✅ Arquivo .env encontrado. Carregando variáveis de ambiente..."
    export $(cat .env | grep -v '#' | xargs)
else
    echo "⚠️ Arquivo .env não encontrado. Usando valores padrão."
fi

# Iniciar a API
echo ""
echo "=========================================================="
echo "✅ INICIANDO API NA PORTA 8000"
echo "=========================================================="
echo ""
echo "Dashboard: http://localhost:8000/"
echo "Health Check: http://localhost:8000/health"
echo ""

python3 -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
