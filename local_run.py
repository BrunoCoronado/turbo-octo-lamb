import json
import sys
from pathlib import Path

# 1. PRIMERO agregamos la carpeta 'src' al path de Python
SRC_PATH = Path(__file__).resolve().parent / "src"
sys.path.append(str(SRC_PATH))

# Importar las funciones Lambda
from client_data.inventory.inventory_handler import lambda_handler as inventory_handler
from client_data.purchases.purchases_handler import lambda_handler as purchases_handler
from client_data.sales.sales_handler import lambda_handler as sales_handler

if __name__ == "__main__":
    # Evento de API Gateway simulado (vaciado por ahora ya que solo es un GET simple)
    fake_event = {
        "httpMethod": "GET",
        "path": "/client-data/inventory",
        "queryStringParameters": None,
        "pathParameters": None
    }
    
    print("--- 1. Probando GET /client-data/inventory ---")
    
    # Invocar directamente el handler (context puede ir como None o un objeto dummy)
    response_inventory = inventory_handler(fake_event, None)
    print("Status Code:", response_inventory["statusCode"])
    print("Body Output:", json.loads(response_inventory["body"])) # Muestra el primer registro
    
    print("--- 2. Probando GET /client-data/purchases ---")
        
    # Invocar directamente el handler (context puede ir como None o un objeto dummy)
    response_inventory = purchases_handler(fake_event, None)
    print("Status Code:", response_inventory["statusCode"])
    print("Body Output:", json.loads(response_inventory["body"])) # Muestra el primer registro
    
    print("--- 3. Probando GET /client-data/sales ---")
        
    # Invocar directamente el handler (context puede ir como None o un objeto dummy)
    response_inventory = sales_handler(fake_event, None)
    print("Status Code:", response_inventory["statusCode"])
    print("Body Output:", json.loads(response_inventory["body"])) # Muestra el primer registro