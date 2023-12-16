import asyncio
from nats.aio.client import Client as NATS
import pytest


@pytest.mark.asyncio
async def test_nats():
    nc = NATS()
    try:
        await nc.connect(servers=["nats://localhost:4222"])
        print("Successfully connected to NATS.")
    except Exception as e:
        print("Failed to connect to NATS:", e)
    finally:
        await nc.close()


if __name__ == '__main__':
    asyncio.run(test_nats())
