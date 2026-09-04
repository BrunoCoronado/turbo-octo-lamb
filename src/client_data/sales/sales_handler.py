from common.response_utils import build_response
from client_data.sales.service import fetch_all_deposits

def lambda_handler(event, context):
    items = fetch_all_deposits()
    return build_response(200, {"content": items})