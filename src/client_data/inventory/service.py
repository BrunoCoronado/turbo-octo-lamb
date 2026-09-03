from pathlib import Path
from common.mock_data_utils import load_mock_data

# Obtiene la ruta del directorio actual donde reside service.py
CURRENT_DIR = Path(__file__).resolve().parent
MOCK_DATA_PATH = CURRENT_DIR / "MOCK_DATA.json"

# Carga de datos al inicializar la Lambda (Caché en memoria para warm starts)
ITEMS_DATA = load_mock_data(MOCK_DATA_PATH)

def fetch_all_movements():
        return ITEMS_DATA