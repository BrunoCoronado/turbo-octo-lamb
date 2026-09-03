import json

def build_response(status_cod: int, body: dict):
    return {
        "statusCode": status_cod,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }