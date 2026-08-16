import asyncio
import time
from datetime import datetime, timezone
from typing import Dict, Any, List

class HealthMonitor:
    def __init__(self, nexus_client, orchestrator):
        self.nexus_client = nexus_client
        self.orchestrator = orchestrator
        self.is_running = False
        self.heartbeats = {}

    async def start(self, interval: int = 60):
        self.is_running = True
        print(f"[HealthMonitor] Iniciado com intervalo de {interval}s")
        while self.is_running:
            await self.check_health()
            await asyncio.sleep(interval)

    async def stop(self):
        self.is_running = False
        print("[HealthMonitor] Parado")

    async def check_health(self):
        now = datetime.now(timezone.utc).isoformat()
        report = {
            "status": "HEALTHY",
            "timestamp": now,
            "components": {
                "orchestrator": "ACTIVE",
                "nexus_bridge": "CONNECTED" if self.nexus_client else "DISCONNECTED",
                "anomaly_count": len(self.orchestrator.anomaly_registry)
            }
        }

        # Simulação de verificação de latência
        if self.nexus_client:
            start_time = time.time()
            messages = await self.nexus_client.get_messages(channel="nexus")
            latency = (time.time() - start_time) * 1000
            report["components"]["nexus_bridge_latency_ms"] = round(latency, 2)
            
            if latency > 3000:
                report["status"] = "DEGRADED"
                await self.orchestrator.fence_anomaly()

        # Reportar no canal nexus
        message = f"[NEXUS-Health-Report] Status: {report['status']} | Latência: {report['components'].get('nexus_bridge_latency_ms', 'N/A')}ms. Orquestrador Operacional."
        if self.nexus_client:
            await self.nexus_client.send_message("Agente-Manus-Orchestrator-Pro", message, channel="nexus", priority="low")
        
        return report
