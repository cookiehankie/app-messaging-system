# EzOut App-to-App Messaging System

## Overview

This document describes the architecture of the EzOut App-to-App Messaging System, designed to facilitate communication between customers using a Swift mobile application and merchant managers using a React web application. The system is crucial for real-time notifications about items being checked out and ensuring efficient store management.

## Components

### Customer Mobile App Component (Swift Application)
- **Functionality**: Allows customers to check out items.
- **Interfaces**: Communicates with the Backend API Service via a REST API.

### Backend API Service Component (FastAPI)
- **Functionality**: 
  - Manages communication and data transfer between components.
  - Implements message scope limitation based on `shop_id`.
  - Optionally, integrates with Firebase for JWT Authentication.
- **Interfaces**: 
  - REST API with endpoints like `/send` and `/publish/{shop_id}`.
  - Connection to NATs.io Component and optionally MongoDB.

### NATs.io Messaging System Component
- **Functionality**: 
  - Manages real-time message distribution.
  - Supports subscription to specific subjects for real-time updates.
- **Interaction**: 
  - Communicates with the Backend API Service and Merchant Web App.

### Merchant Web App Component (React Application)
- **Functionality**: Displays real-time data and updates based on specific Store IDs.
- **Interfaces**: Receives updates from the NATs.io Component.

### Database Component (MongoDB)
- **Functionality**: Stores messages and logs activity.
- **Integration**: Utilizes MongoDB change streams for real-time data capture.

### Firebase Authentication Service 
- **Functionality**: Provides user authentication.
- **Integration**: Integrated with the Backend API Service for authentication.

## Data Flow

- Data flows from the Customer Mobile App to the Backend API Service.
- The Backend API Service communicates with NATs.io and optionally with MongoDB.
- NATs.io sends updates to the Merchant Web App.
- Backend API Service integrates with Firebase for authentication (optional).

## Docker Compose and Deployment

- Docker Compose is used for orchestrating the Backend API, Frontend Applications, NATs.io, and optionally MongoDB.
- A Dockerfile may be provided for custom configurations of NATs.io.

## Additional Notes

- Authentication: While JWT Authentication is conceptually included, its implementation using Firebase is suggested for future development.
- Real-Time Data: MongoDB change streams can be leveraged for capturing real-time checkout notifications.
