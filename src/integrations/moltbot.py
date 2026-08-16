import aiohttp
import json
from typing import Dict, Any

class MoltbotClient:
    def __init__(self, webhook_url: str, auth_token: str):
        self.webhook_url = webhook_url
        self.auth_token = auth_token

    async def send_command(self, command_type: str, command_args: str, description: str) -> Dict[str, Any]:
        payload = {
            "command_type": command_type,
            "command_args": command_args,
            "description": description,
            "auth_token": self.auth_token # Incluir o token de autenticação
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}" # Pode ser usado para autenticação no webhook
        }

        print(f"[MoltbotClient] Enviando comando para {self.webhook_url}: {payload}")

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.webhook_url, json=payload, headers=headers) as response:
                    response.raise_for_status()  # Levanta exceção para status HTTP 4xx/5xx
                    result = await response.json()
                    print(f"[MoltbotClient] Resposta recebida: {result}")
                    return result
            except aiohttp.ClientError as e:
                print(f"[MoltbotClient] Erro ao enviar comando: {e}")
                return {"status": "error", "message": str(e)}
            except json.JSONDecodeError:
                text = await response.text()
                print(f"[MoltbotClient] Erro ao decodificar JSON: {text}")
                return {"status": "error", "message": f"Resposta não é JSON: {text}"}

if __name__ == '__main__':
    async def main():
        # Exemplo de uso (substitua pela sua URL e token reais)
        MOLTBOT_WEBHOOK_URL = "http://localhost:8080/moltbot-webhook" # Exemplo
        MOLTBOT_AUTH_TOKEN = "your_moltbot_secret_token" # Exemplo

        client = MoltbotClient(MOLTBOT_WEBHOOK_URL, MOLTBOT_AUTH_TOKEN)

        print("\n--- Teste: Abrir navegador ---")
        response = await client.send_command("browser_navigate", "https://www.google.com", "Abrir Google")
        print(response)

        print("\n--- Teste: Executar comando shell ---")
        response = await client.send_command("shell", "ls -la", "Listar arquivos")
        print(response)

    import asyncio
    asyncio.run(main())
