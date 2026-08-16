from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.orchestrator import AutonomousOrchestrator
from core.health_monitor import HealthMonitor
from integrations.moltbot import MoltbotClient
from integrations.nexus import NexusClient

app = FastAPI(title="Autonomous Orchestrator API (NEXUS Symbiosis Edition)", version="1.1.0")

# Configurações via Variáveis de Ambiente
MOLTBOT_WEBHOOK_URL = os.getenv("MOLTBOT_WEBHOOK_URL", "http://localhost:8080/moltbot-webhook")
MOLTBOT_AUTH_TOKEN = os.getenv("MOLTBOT_AUTH_TOKEN", "your_moltbot_secret_token")
SIAOL_BASE_URL = os.getenv("SIAOL_BASE_URL", "https://urijah-metaphrastical-gorily.ngrok-free.dev")
SIAOL_BEARER_TOKEN = os.getenv("SIAOL_BEARER_TOKEN")

# Inicializar Clientes
moltbot_client = MoltbotClient(MOLTBOT_WEBHOOK_URL, MOLTBOT_AUTH_TOKEN)
nexus_client = None
if SIAOL_BEARER_TOKEN:
    nexus_client = NexusClient(SIAOL_BASE_URL, SIAOL_BEARER_TOKEN)

# Inicializar o Orquestrador
orchestrator = AutonomousOrchestrator(moltbot_client, nexus_client)
health_monitor = HealthMonitor(nexus_client, orchestrator)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(health_monitor.start(interval=300)) # Monitoramento a cada 5 min

# Modelos Pydantic
class TaskRequest(BaseModel):
    description: str
    priority: str = "normal"

class TaskResponse(BaseModel):
    task_id: str
    status: str
    results: List[Dict[str, Any]]

@app.get("/")
async def root():
    return {
        "message": "Autonomous Orchestrator API - NEXUS Edition",
        "version": "1.1.0",
        "nexus_status": "connected" if nexus_client else "disconnected",
        "endpoints": {
            "POST /tasks": "Criar uma nova tarefa",
            "GET /tasks/{task_id}": "Obter status de uma tarefa",
            "GET /nexus/anomalies": "Listar anomalias cercadas",
            "POST /webhooks/moltbot": "Receber callbacks do Moltbot"
        }
    }

@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskRequest):
    try:
        print(f"Recebida tarefa: {task.description}")
        results = await orchestrator.run_task(task.description)
        return TaskResponse(
            task_id="task_001",
            status="completed",
            results=results
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nexus/anomalies")
async def get_anomalies():
    return {
        "count": len(orchestrator.anomaly_registry),
        "anomalies": orchestrator.anomaly_registry
    }

@app.post("/webhooks/moltbot")
async def moltbot_webhook(payload: Dict[str, Any]):
    print(f"Webhook do Moltbot recebido: {payload}")
    return {"status": "received", "message": "Webhook processado com sucesso"}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "moltbot_connected": True,
        "nexus_connected": nexus_client is not None,
        "orchestrator_ready": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
