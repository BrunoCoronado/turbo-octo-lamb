from client_data.sales.queries import build_all_deposits_query
from common.athena_client import AthenaService

def fetch_all_deposits():
    query = build_all_deposits_query()
    athena_service = AthenaService()
    data = athena_service.run(query)
    return data