import json
from app import app, db
from resources.item import Item

def test_add_item():
    with app.test_client() as client:
        response = client.post('/items', json={'name': 'Laptop', 'price': 999.99})
        assert response.status_code == 201
        assert 'id' in response.get_json()

def test_get_items():
    with app.test_client() as client:
        response = client.get('/items')
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

def test_get_item():
    with app.test_client() as client:
        response = client.post('/items', json={'name': 'Phone', 'price': 499.99})
        item_id = response.get_json()['id']
        
        response = client.get(f'/items/{item_id}')
        assert response.status_code == 200
        assert response.get_json()['name'] == 'Phone'

def test_update_item():
    with app.test_client() as client:
        response = client.post('/items', json={'name': 'Tablet', 'price': 349.99})
        item_id = response.get_json()['id']
        
        response = client.put(f'/items/{item_id}', json={'name': 'Tablet Pro', 'price': 499.99})
        assert response.status_code == 200
        assert response.get_json()['message'] == 'Item updated'

def test_delete_item():
    with app.test_client() as client:
        response = client.post('/items', json={'name': 'Watch', 'price': 199.99})
        item_id = response.get_json()['id']
        
        response = client.delete(f'/items/{item_id}')
        assert response.status_code == 200
        assert response.get_json()['message'] == 'Item deleted'
