import json
import sys
from pathlib import Path

# 1. PRIMERO agregamos la carpeta 'src' al path de Python
SRC_PATH = Path(__file__).resolve().parent / "src"
sys.path.append(str(SRC_PATH))

# Importar las funciones Lambda
from client_data.inventory.inventory_handler import lambda_handler as inventory_handler

if __name__ == "__main__":
    print("--- 1. Probando GET /client-data/inventory ---")
    # Evento de API Gateway simulado (vaciado por ahora ya que solo es un GET simple)
    fake_event = {
        "httpMethod": "GET",
        "path": "/client-data/inventory",
        "queryStringParameters": None,
        "pathParameters": None
    }
    
    # Invocar directamente el handler (context puede ir como None o un objeto dummy)
    response_inventory = inventory_handler(fake_event, None)
    print("Status Code:", response_inventory["statusCode"])
    print("Body Output:", json.loads(response_inventory["body"])) # Muestra el primer registro