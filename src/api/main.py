from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio
import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.orchestrator import AutonomousOrchestrator
from integrations.moltbot import MoltbotClient

app = FastAPI(title="Autonomous Orchestrator API", version="1.0.0")

# Configuração do Moltbot
MOLTBOT_WEBHOOK_URL = os.getenv("MOLTBOT_WEBHOOK_URL", "http://localhost:8080/moltbot-webhook")
MOLTBOT_AUTH_TOKEN = os.getenv("MOLTBOT_AUTH_TOKEN", "your_moltbot_secret_token")

# Inicializar o cliente do Moltbot
moltbot_client = MoltbotClient(MOLTBOT_WEBHOOK_URL, MOLTBOT_AUTH_TOKEN)

# Inicializar o Orquestrador
orchestrator = AutonomousOrchestrator(moltbot_client)

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
        "message": "Autonomous Orchestrator API",
        "version": "1.0.0",
        "endpoints": {
            "POST /tasks": "Criar uma nova tarefa",
            "GET /tasks/{task_id}": "Obter status de uma tarefa",
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

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    # Simulação: em um cenário real, isso consultaria um banco de dados
    return {
        "task_id": task_id,
        "status": "completed",
        "results": []
    }

@app.post("/webhooks/moltbot")
async def moltbot_webhook(payload: Dict[str, Any]):
    print(f"Webhook do Moltbot recebido: {payload}")
    # Aqui você pode processar o callback do Moltbot
    return {"status": "received", "message": "Webhook processado com sucesso"}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "moltbot_connected": True,
        "orchestrator_ready": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
