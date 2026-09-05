import json
import pytest

from client_data.inventory.inventory_handler import lambda_handler as inventory_handler
from client_data.purchases.purchases_handler import lambda_handler as purchases_handler
from client_data.sales.sales_handler import lambda_handler as sales_handler

@pytest.fixture
def mock_event():
    return {
        "headers": {"Content-Type": "application/json"},
        "requestContext": {"http": {"method": "GET"}}
    }

def test_lambda_inventory(mock_event):
    response = inventory_handler(mock_event, None)
    
    assert response["statusCode"] == 200
    assert "body" in response
    
def test_lambda_purchases(mock_event):
    response = purchases_handler(mock_event, None)
    
    assert response["statusCode"] == 200
    assert "body" in response
    
def test_lambda_sales(mock_event):
    response = sales_handler(mock_event, None)
    
    assert response["statusCode"] == 200
    assert "body" in response