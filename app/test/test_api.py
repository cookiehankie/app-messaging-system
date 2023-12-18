"""
This test is designed to verify that
the /publish/{shop_id} endpoint in the FastAPI application
correctly publishes a message to a NATS server.
"""


from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from app.main import app
from uuid import UUID
import json
from datetime import datetime

client = TestClient(app)


def test_publish_message():
    # Define the shop_id and message_data for testing
    shop_id = UUID("123e4567-e89b-42d3-a456-426614174000")
    message_data = {
        "session_id": "4e29b2d3-7c8a-446e-a4e1-d8e2a51c0e94",
        "shop_id": str(shop_id),
        "shopper_id": "ab29b2d3-7c8a-446e-a4e1-d8e2a51c0e94",
        "action_id": 101,
        'create_time': '2023-12-13T10:30:00.000Z',
        "action": "ADD",
        "product_name": "Fresh Apples",
        "product_id": 500100,
        "product_price": 3.50,
        "UPC": "042100005264",
        "category_id": "fruit",
        "basket_total": 10.60
    }

    # Patch the nc.publish method from your app.nats module
    with patch("app.nats.nc.publish", new_callable=AsyncMock) as mock_publish:
        response = client.post(f"/publish/{shop_id}", json=message_data)

        assert response.status_code == 200
        assert response.json() == {"status": f"Message sent to shop ID {shop_id}"}

        mock_publish.assert_awaited_once()
        called_args, called_kwargs = mock_publish.call_args_list[0]

        assert called_args[0] == f"updates.store.{shop_id}"

        published_data = json.loads(called_args[1].decode())
        # Adjusting the create_time format for comparison
        message_data['create_time'] = datetime.fromisoformat(message_data['create_time'].replace('Z', '+00:00')).isoformat()
        published_data['create_time'] = datetime.fromisoformat(published_data['create_time']).isoformat()

        assert message_data == published_data


# This allows you to run the test with `python test_api.py`
if __name__ == "__main__":
    test_publish_message()
