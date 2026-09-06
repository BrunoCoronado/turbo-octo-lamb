from client_data.inventory.queries import build_inventory_movements_query
from common.athena_client import AthenaService

def fetch_all_movements():
        query = build_inventory_movements_query()
        athena_service = AthenaService()
        data = athena_service.run(query)
        return data