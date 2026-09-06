import os

def build_purchases_details_query() -> str:
    db_name = os.environ.get('ATHENA_DATABASE_NAME', 'turbo_octo_lamb')
    
    return f"""
        SELECT 
            itemPurchaseId,
            businessDate,
            itemPurchaseReferenceNumber,
            itemPurchaseComment
        FROM {db_name}.purchases;
    """