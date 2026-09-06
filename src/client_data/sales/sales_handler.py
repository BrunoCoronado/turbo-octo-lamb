from common.response_utils import build_response
from client_data.sales.service import fetch_all_deposits

def lambda_handler(event, context):
    try:
        items = fetch_all_deposits()
        return build_response(200, {
            "status": "sucsess",
            "count": len(items),
            "content": items
        })
    except Exception as e:
        return build_response(500, {
            "status": "error",
            "message": str(e)
        })
