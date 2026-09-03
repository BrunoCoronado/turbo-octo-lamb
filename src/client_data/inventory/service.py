import json
from pathlib import Path

# Obtiene la ruta del directorio actual donde reside service.py
CURRENT_DIR = Path(__file__).resolve().parent
MOCK_DATA_PATH = CURRENT_DIR / "MOCK_DATA.json"

def _load_mock_data() -> list[dict]:
    """Carga y parsea el archivo JSON."""
    try:
        with open(MOCK_DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {MOCK_DATA_PATH}")
        return []
    
# Carga de datos al inicializar la Lambda (Caché en memoria para warm starts)
ITEMS_DATA = _load_mock_data()

def fetch_all_movements():
        return ITEMS_DATA