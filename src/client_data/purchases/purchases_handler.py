from common.response_utils import build_response
from client_data.purchases.service import fetch_all_details

def lambda_handler(event, context):
    items = fetch_all_details()
    return build_response(200, {"content": items})