# App Messaging System

## Overview
The App Messaging System is designed to streamline communication between customers and merchant managers through a Swift application for customers and a React web application for merchants. It leverages a FastAPI backend to facilitate real-time messaging and data handling.

## System Components
- **Customer App (Swift)**: A mobile application for customers to perform item checkouts.
- **Backend API Service (FastAPI)**: A robust backend service to process and relay messages.
- **Merchant Manager App (React)**: A web application for merchants to receive real-time updates.

## Data Flow Diagram
```plantuml
@startuml
[Customer App - Swift] --> [Backend API Service - FastAPI] : sends checkout data via REST API
[Backend API Service - FastAPI] --> [MongoDB] : logs data (optional)
[Backend API Service - FastAPI] --> [NATs.io Messaging System] : publishes messages
[NATs.io Messaging System] --> [Merchant Manager App - React] : sends real-time updates
@enduml
