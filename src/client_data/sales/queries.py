import os

def build_all_deposits_query() -> str:
    db_name = os.environ.get('ATHENA_DATABASE_NAME', 'turbo_octo_lamb')
    
    return f"""
        SELECT 
            depositId,
            depositTime,
            businessDate,
            salesAreaName,
            voucherNumber
        FROM {db_name}.sales;
    """