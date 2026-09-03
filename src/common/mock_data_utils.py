import json

def load_mock_data(mock_data_path: str) -> list[dict]:
    """Carga y parsea el archivo JSON."""
    try:
        with open(mock_data_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {mock_data_path}")
        return []