# app-messaging-system
An app-to-app messaging system to facilitate communication between customers using a Swift application and merchant managers using a React web application.

[Customer App - Swift] --> [Backend API Service - FastAPI] : sends checkout data via REST API

[Backend API Service - FastAPI] --> [MongoDB] : logs data (optional)

[Backend API Service - FastAPI] --> [NATs.io Messaging System] : publishes messages

[NATs.io Messaging System] --> [Merchant Manager App - React] : sends real-time updates
