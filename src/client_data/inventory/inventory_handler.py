from common.response_utils import build_response
from client_data.inventory.service import fetch_all_movements

def lambda_handler(event, context):
    items = fetch_all_movements()
    return build_response(200, {"content": items})