import aiohttp
import json
import os
from typing import Dict, Any, List

class NexusClient:
    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    async def get_messages(self, channel: str = "symbiosis") -> List[Dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.base_url}/messages/{channel}", headers=self.headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data.get("messages", [])
            except Exception as e:
                print(f"[NexusClient] Erro ao buscar mensagens: {e}")
                return []

    async def send_message(self, sender: str, content: str, channel: str = "symbiosis", priority: str = "medium") -> Dict[str, Any]:
        payload = {
            "sender": sender,
            "channel": channel,
            "content": content,
            "priority": priority,
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(f"{self.base_url}/message", headers=self.headers, json=payload) as response:
                    response.raise_for_status()
                    return await response.json()
            except Exception as e:
                print(f"[NexusClient] Erro ao enviar mensagem: {e}")
                return {"status": "error", "message": str(e)}
