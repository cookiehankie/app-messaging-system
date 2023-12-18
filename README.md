# EzOut App-to-App Messaging System

## Overview

The EzOut App-to-App Messaging System is engineered to streamline communication between the Swift-based customer application and the React-based merchant management application. It plays a pivotal role in broadcasting real-time notifications pertinent to item checkouts, thus enhancing the efficacy of store management operations.

## System Architecture

![app-messaging-system](https://github.com/cookiehankie/app-messaging-system/assets/106795225/0f675d87-736e-42ad-a240-4e19569f205d)

## Feature Visualization
### Postman
 - POST
```
http://localhost:8000/publish/{shop_id}
```
```
http://localhost:8000/publish/123e4567-e89b-42d3-a456-426614174000
```
- Body: JSON
```json
{
    "session_id": "4e29b2d3-7c8a-446e-a4e1-d8e2a51c0e94",
    "shop_id": "123e4567-e89b-42d3-a456-426614174000",
    "shopper_id": "ab29b2d3-7c8a-446e-a4e1-d8e2a51c0e94",
    "action_id": 101,
    "create_time": "2023-12-18T10:30:00.000Z",
    "action": "ADD",
    "product_name": "FUJI Apples",
    "product_id": 500100,
    "product_price": 3.50,
    "UPC": "042100005264",
    "category_id": "fruit",
    "basket_total": 12.18
}
```
 - Output
```json
{
    "status": "Message sent to shop ID 123e4567-e89b-42d3-a456-426614174000"
}
```
### Terminal
```python
# Publish the message to the NATs server
subject = f"updates.store.{shop_id}"
```

 ```shell
nats sub XXX -s nats://localhost:4222
```

```shell
nats sub updates.store.123e4567-e89b-42d3-a456-426614174000 -s nats://localhost:4222
```

```
Subscribing on updates.store.123e4567-e89b-42d3-a456-426614174000
```
- Updates after the POST
```
[#1] Received on "updates.store.123e4567-e89b-42d3-a456-426614174000"
{"session_id": "4e29b2d3-7c8a-446e-a4e1-d8e2a51c0e94", "shop_id": "123e4567-e89b-42d3-a456-426614174000", "shopper_id": "ab29b2d3-7c8a-446e-a4e1-d8e2a51c0e94", "action_id": 101, "create_time": "2023-12-18 10:30:00+00:00", "action": "ADD", "product_name": "FUJI Apples", "product_id": 500100, "product_price": 3.5, "UPC": "042100005264", "category_id": "fruit", "basket_total": 12.18}
```
- Match with the JSON file we POSTed

**Additionally**,
**we can automate this message-receiving test by running the file `test/test_api.py`**

## Components
### Customer Mobile App (Swift)

**Functionality**:
  - Facilitates customers in checking out items seamlessly.

**Interfaces**:
  - Engages in data exchange with the Backend API Service via RESTful calls.

### Backend API Service (FastAPI)

**Functionality**:
  - Serves as the central hub for data and message transit between the system's components.
  - Enforces message delivery constraints by `shop_id` to ensure targeted communication.
  - Offers integration capabilities with Firebase for robust JWT Authentication.

**Interfaces**:
  - Hosts RESTful endpoints `/send` and `/publish/{shop_id}` for message dispatching.
  - Establishes connectivity with the NATs.io Messaging System and optionally with MongoDB for data persistence.

### NATs.io Messaging System

**Functionality**:
  - Orchestrates the distribution of messages in real-time.
  - Permits subscription to specified topics to enable instantaneous updates.

**Interaction**:
  - Facilitates bi-directional communication with the Backend API Service and the Merchant Web App.

### Resgate

**Functionality**:
  - Provides a real-time API gateway for the NATS.io messaging system, enabling REST and WebSocket connections.

**Integration**:
  - Bridges the gap between the frontend applications and the NATS.io system, offering real-time synchronization capabilities.

### Merchant Web App (React)

**Functionality**:
  - Exhibits real-time data and updates congruent with specified Store IDs.

**Interfaces**:
  - Accepts and displays notifications from the NATs.io Messaging System.

### Database (MongoDB)

**Functionality**:
  - Archives messages and logs transactional activities.

**Integration**:
  - Employs MongoDB change streams to track and transmit real-time data alterations.

### Firebase Authentication Service

**Functionality**:
  - Administers user authentication processes.

**Integration**:
  - Seamlessly integrates with the Backend API Service to authenticate users.

## Data Flow

1. The Customer Mobile App dispatches checkout data to the Backend API Service.
2. The Backend API Service processes the data and publishes it to the NATs.io Messaging System.
3. Resgate listens to NATs.io for new messages and transforms the NATS messaging into WebSockets or HTTP responses.
4. The Merchant Web App subscribes to Resgate to receive real-time updates through WebSocket connections or HTTP streaming, enabling a reactive user interface that reflects changes in real-time.
5. If integrated, MongoDB stores the transaction records and the Backend API Service can react to changes via MongoDB change streams, which can also be published to NATs.io for additional real-time updates.
6. The Backend API Service, if configured, uses Firebase for user authentication, which controls access to the publishing and subscribing of messages.


## Docker Compose and Deployment
  - Docker Compose is used for orchestrating the Backend API, NATs.io, Resgate and Frontend.

## Additional Notes

**Authentication**: The system's design includes JWT Authentication, with a recommended future integration of Firebase to implement this feature.

**Real-Time Data**: For capturing real-time checkout notifications, the system can utilize MongoDB change streams, adding another layer of responsiveness to the merchant's operations.
