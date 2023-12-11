# app-messaging-system
An app-to-app messaging system to facilitate communication between customers using a Swift application and merchant managers using a React web application.

   +------------------+ 
   |                  |
   | Customer App     |
   | (Swift)          | 
   |                  |
   +---------+--------+
             |
             | sends checkout data
             | via REST API
   +---------+--------+
   |                  | 
   | Backend API      |
   | Service          |
   | (FastAPI)        |
   |                  |
   +---------+--------+
             |
             |logs data (optional)
             |
   +---------+--------+
   |                  |
   | MongoDB          |
   |                  |
   +---------+--------+
             |
             |publishes messages
             |
   +---------+--------+
   |                  |
   | NATs.io          |
   | Messaging System |
   |                  | 
   +---------+--------+
             |
             |sends real-time
             |updates
   +---------+--------+
   |                  |
   | Merchant         |
   | Manager App      |
   | (React)          |
   |                  |
   +------------------+