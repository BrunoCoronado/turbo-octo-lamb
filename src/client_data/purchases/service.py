from client_data.purchases.queries import build_purchases_details_query
from common.athena_client import AthenaService

def fetch_all_details():
    query = build_purchases_details_query()
    athena_service = AthenaService()
    data = athena_service.run(query)
    return data