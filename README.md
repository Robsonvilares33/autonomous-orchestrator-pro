# Autonomous Orchestrator Pro

**Um sistema de orquestração autônoma que integra inteligência de IA com execução local via Moltbot.**

## 🎯 Visão Geral

O **Autonomous Orchestrator Pro** é uma plataforma de automação inteligente que combina:

- **Orquestração de Tarefas**: Decomposição automática de tarefas complexas em subtarefas executáveis
- **Integração Moltbot**: Controle direto do computador local para execução de comandos, navegação web e manipulação de arquivos
- **API RESTful**: Interface moderna para submissão e acompanhamento de tarefas
- **Escalabilidade**: Suporte para múltiplas tarefas concorrentes com timeout configurável

## 🚀 Características

- ✅ Decomposição inteligente de tarefas
- ✅ Integração com Moltbot para execução local
- ✅ API FastAPI moderna e documentada
- ✅ Suporte para Docker e Docker Compose
- ✅ Logging detalhado e monitoramento
- ✅ Configuração via variáveis de ambiente
- ✅ Health checks e status monitoring

## 📋 Requisitos

- Python 3.8+
- Docker e Docker Compose (opcional)
- Moltbot instalado e rodando no computador local
- pip3 para gerenciamento de dependências

## 🔧 Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/autonomous-orchestrator-pro.git
cd autonomous-orchestrator-pro
```

### 2. Criar Ambiente Virtual (Opcional mas Recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip3 install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🏃 Como Usar

### Iniciar via Script

```bash
chmod +x scripts/start_orchestrator.sh
./scripts/start_orchestrator.sh
```

### Iniciar via Python Direto

```bash
python3 -m uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

### Iniciar via Docker

```bash
docker-compose up --build
```

## 📡 API Endpoints

### GET `/`
Retorna informações sobre a API.

```bash
curl http://localhost:8000/
```

### POST `/tasks`
Cria uma nova tarefa.

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Abra o navegador e acesse o Google",
    "priority": "normal"
  }'
```

### GET `/tasks/{task_id}`
Obtém o status de uma tarefa.

```bash
curl http://localhost:8000/tasks/task_001
```

### POST `/webhooks/moltbot`
Recebe callbacks do Moltbot.

```bash
curl -X POST http://localhost:8000/webhooks/moltbot \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "task_001",
    "status": "completed",
    "result": "Sucesso"
  }'
```

### GET `/health`
Verifica o status de saúde da API.

```bash
curl http://localhost:8000/health
```

## 🔌 Configuração do Moltbot

### 1. Instalar o Moltbot

Siga as instruções em [https://moltbot.io/](https://moltbot.io/)

### 2. Configurar o Webhook

No seu arquivo `.env`:

```env
MOLTBOT_WEBHOOK_URL=http://localhost:8080/moltbot-webhook
MOLTBOT_AUTH_TOKEN=seu_token_secreto
```

### 3. Testar a Conexão

```bash
curl -X POST http://localhost:8080/moltbot-webhook \
  -H "Content-Type: application/json" \
  -d '{
    "command_type": "shell",
    "command_args": "echo teste",
    "description": "Teste de conexão"
  }'
```

## 📂 Estrutura do Projeto

```
autonomous-orchestrator-pro/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   └── orchestrator.py          # Lógica principal de orquestração
│   ├── integrations/
│   │   ├── __init__.py
│   │   └── moltbot.py               # Cliente do Moltbot
│   ├── api/
│   │   ├── __init__.py
│   │   └── main.py                  # API FastAPI
│   ├── tools/
│   │   ├── __init__.py
│   │   └── mcp_tools.py             # Ferramentas MCP
│   └── __init__.py
├── config/
│   └── settings.py                  # Configurações da aplicação
├── scripts/
│   └── start_orchestrator.sh         # Script de inicialização
├── .env                             # Variáveis de ambiente
├── .env.example                     # Exemplo de variáveis
├── Dockerfile                       # Imagem Docker
├── docker-compose.yml               # Composição Docker
├── requirements.txt                 # Dependências Python
└── README.md                        # Este arquivo
```

## 🧪 Testes

### Teste 1: Abrir Navegador

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Abra o navegador e acesse o Google",
    "priority": "normal"
  }'
```

### Teste 2: Executar Comando Shell

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Execute um comando ls -la",
    "priority": "normal"
  }'
```

### Teste 3: Verificar Health

```bash
curl http://localhost:8000/health
```

## 🔐 Segurança

- ✅ Autenticação via token no Moltbot
- ✅ Validação de payloads JSON
- ✅ Isolamento de tarefas
- ✅ Timeout de tarefas configurável
- ✅ Logging detalhado de todas as operações

## 📊 Monitoramento

### Logs

Os logs são salvos em `orchestrator.log` por padrão. Você pode configurar o nível de log:

```env
LOG_LEVEL=DEBUG  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### Health Check

```bash
curl http://localhost:8000/health
```

Resposta esperada:
```json
{
  "status": "healthy",
  "moltbot_connected": true,
  "orchestrator_ready": true
}
```

## 🚀 Deployment

### Deploy Local

```bash
./scripts/start_orchestrator.sh
```

### Deploy com Docker

```bash
docker-compose up -d
```

### Deploy em Produção

Para produção, considere:

1. Usar um gerenciador de processos (systemd, supervisor)
2. Configurar um reverse proxy (nginx, Apache)
3. Usar HTTPS/SSL
4. Configurar rate limiting
5. Implementar autenticação robusta

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato através de:

- Email: support@example.com
- Discord: [Link do servidor]
- GitHub Issues: [Link do repositório]

## 🙏 Agradecimentos

- Moltbot pela integração local
- FastAPI pela excelente framework
- Comunidade Python

---

**Desenvolvido com ❤️ por Manus AI**

*Sua automação inteligente e autônoma começa aqui!*
