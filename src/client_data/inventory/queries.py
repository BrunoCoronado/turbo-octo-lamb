import os

def build_inventory_movements_query() -> str:
    db_name = os.environ.get('ATHENA_DATABASE_NAME', 'turbo_octo_lamb')
    
    return f"""
        SELECT 
            inventoryItemCode,
            inventoryItemId,
            inventoryItemDescription,
            initialInventory,
            mov,
            value
        FROM {db_name}.inventory;
    """