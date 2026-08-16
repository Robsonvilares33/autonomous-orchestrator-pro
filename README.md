# Autonomous Orchestrator Pro (NEXUS Symbiosis Edition)

**Um sistema de orquestração autônoma que integra inteligência de IA com execução local via Moltbot, operando em simbiose na infraestrutura universal NEXUS.**

## 🎯 Visão Geral

O **Autonomous Orchestrator Pro** é uma plataforma de automação inteligente que combina:

- **Orquestração de Tarefas**: Decomposição automática de tarefas complexas em subtarefas executáveis.
- **Integração Moltbot**: Controle direto do computador local para execução de comandos, navegação web e manipulação de arquivos.
- **Rede de Simbiose SIAOL-PRO**: Conexão nativa via API REST Gateway para colaboração multi-agente (Antigravity, Manus-01, Orchestrator-Pro) no ecossistema NEXUS.
- **API RESTful**: Interface moderna para submissão e acompanhamento de tarefas.

## 🚀 Características

- ✅ Decomposição inteligente de tarefas.
- ✅ Integração com Moltbot para execução local.
- ✅ Protocolo de Simbiose Multi-Agente integrado (NEXUS).
- ✅ API FastAPI moderna e documentada.
- ✅ Suporte para Docker e Docker Compose.
- ✅ Logging detalhado e monitoramento.

## 📋 Requisitos

- Python 3.8+
- Docker e Docker Compose (opcional)
- Moltbot instalado e rodando no computador local
- Token de acesso à Ponte Neural SIAOL-PRO

## 🔧 Instalação e Integração

### 1. Clonar o Repositório

```bash
git clone https://github.com/Robsonvilares33/autonomous-orchestrator-pro.git
cd autonomous-orchestrator-pro
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` baseado no exemplo e configure suas chaves:

```env
PORT=8000
MOLTBOT_WEBHOOK_URL=http://localhost:3000/webhook
SIAOL_BEARER_TOKEN=<defina-via-variavel-de-ambiente>
```

### 3. Executar o Orquestrador

```bash
./scripts/start_orchestrator.sh
```

---
*Desenvolvido em simbiose para a Missão NEXUS (Prazo: 25/08).*
