import json

def get_mcp_tools():
    return [
        {
            "name": "local_execution_trigger",
            "description": "Executa um comando ou script no computador local do usuário via Moltbot. Use para tarefas que exigem controle direto do sistema operacional, como abrir aplicativos, manipular arquivos locais, interagir com o navegador ou executar scripts personalizados. O Moltbot deve estar configurado e rodando na máquina do usuário.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "O comando ou script a ser executado no terminal local. Pode ser um comando de shell (ex: 'ls -la', 'open /Applications/Google Chrome.app'), um script Python (ex: 'python3 /path/to/script.py'), ou uma instrução para o navegador (ex: 'browser_navigate https://www.google.com')."
                    },
                    "description": {
                        "type": "string",
                        "description": "Uma breve descrição da ação que será executada, para fins de log e acompanhamento."
                    }
                },
                "required": [
                    "command",
                    "description"
                ]
            }
        }
    ]

if __name__ == '__main__':
    # Exemplo de uso para gerar o JSON de ferramentas
    tools = get_mcp_tools()
    print(json.dumps(tools, indent=2))
