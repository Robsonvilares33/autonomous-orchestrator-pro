import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do Moltbot
MOLTBOT_WEBHOOK_URL = os.getenv("MOLTBOT_WEBHOOK_URL", "http://localhost:8080/moltbot-webhook")
MOLTBOT_AUTH_TOKEN = os.getenv("MOLTBOT_AUTH_TOKEN", "your_moltbot_secret_token")

# Configurações da API
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
API_DEBUG = os.getenv("API_DEBUG", "False").lower() == "true"

# Configurações do Orquestrador
ORCHESTRATOR_MAX_CONCURRENT_TASKS = int(os.getenv("ORCHESTRATOR_MAX_CONCURRENT_TASKS", 4))
ORCHESTRATOR_TASK_TIMEOUT = int(os.getenv("ORCHESTRATOR_TASK_TIMEOUT", 300))  # 5 minutos

# Configurações de Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "orchestrator.log")

# Configurações de Banco de Dados (se necessário)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./orchestrator.db")

print(f"""
=== Configurações do Autonomous Orchestrator ===
Moltbot Webhook URL: {MOLTBOT_WEBHOOK_URL}
API Host: {API_HOST}
API Port: {API_PORT}
Debug Mode: {API_DEBUG}
Max Concurrent Tasks: {ORCHESTRATOR_MAX_CONCURRENT_TASKS}
Task Timeout: {ORCHESTRATOR_TASK_TIMEOUT}s
Log Level: {LOG_LEVEL}
""")
