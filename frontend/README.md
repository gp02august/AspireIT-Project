# Full-Stack Childcare Management System

This project is a **Full-Stack Childcare Management System** built using **Flask** for the backend. The backend provides APIs for managing user authentication, children, caregivers, finances, attendance, and enrollment records. It also supports pagination for fetching children, user registration, and login using JWT-based authentication.

## Features

- **User Authentication**: Register and login using JWT authentication.
- **Children Management**: Add, update, retrieve, and delete children.
- **Caregiver Management**: Manage caregivers related to children.
- **Financial Records**: CRUD operations for tracking financial transactions.
- **Attendance Tracking**: Record and retrieve attendance details for children.
- **Enrollment Records**: Manage children's enrollment information.
- **Swagger API Documentation**: Provides Swagger UI for easy API documentation.
- **CORS Enabled**: Configured to allow cross-origin requests (useful for connecting with frontend).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Backend Routes](#backend-routes)
- [Models](#models)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [License](#license)

---

## Installation

1. Clone this repository:

   ```bash
   git clone <repo_url>
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Set up a PostgreSQL database, and update the `.env` file with the database URL and secret key.

   Example `.env`:

   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/childcare_db
   SECRET_KEY=your_jwt_secret_key
   ```
4. Run the database migrations:

   ```bash
   flask db upgrade
   ```
5. Start the Flask server:

   ```bash
   flask run
   ```

---

## Backend Routes

### User Routes

- **POST /api/register** - Register a new user.
- **POST /api/login** - Login and obtain a JWT token.

### Children Routes

- **GET /api/children** - Retrieve paginated list of children (requires JWT).
- **POST /api/children** - Add a new child (requires JWT).
- **GET /api/children/\<child_id\>** - Retrieve details of a specific child (requires JWT).
- **PUT /api/children/\<child_id\>** - Update a specific child's details (requires JWT).
- **DELETE /api/children/\<child_id\>** - Delete a specific child (requires JWT).

### Caregiver Routes

- **GET /api/caregivers** - Retrieve list of all caregivers (requires JWT).

### Finance Routes

- **POST /api/finances** - Add a new financial transaction (requires JWT).
- **GET /api/finances** - Retrieve list of financial transactions (requires JWT).

### Attendance Routes

- **POST /api/attendance** - Add a new attendance record (requires JWT).
- **GET /api/attendance** - Retrieve attendance records (requires JWT).

### Enrollment Routes

- **POST /api/enrollments** - Add a new enrollment record (requires JWT).
- **GET /api/enrollments** - Retrieve enrollment records (requires JWT).

---

## Models

### User

| Field    | Type    | Description     |
| -------- | ------- | --------------- |
| id       | Integer | Primary key     |
| username | String  | Unique username |
| password | String  | Hashed password |

### Children

| Field     | Type    | Description              |
| --------- | ------- | ------------------------ |
| id        | Integer | Primary key              |
| name      | String  | Name of the child        |
| age       | Integer | Age of the child         |
| caregiver | Foreign | Foreign key to Caregiver |

### Caregiver

| Field | Type    | Description           |
| ----- | ------- | --------------------- |
| id    | Integer | Primary key           |
| name  | String  | Name of the caregiver |

### Finance

| Field       | Type    | Description                    |
| ----------- | ------- | ------------------------------ |
| id          | Integer | Primary key                    |
| amount      | Float   | Amount of the transaction      |
| description | String  | Description of the transaction |
| date        | Date    | Date of the transaction        |

### Attendance

| Field    | Type    | Description             |
| -------- | ------- | ----------------------- |
| id       | Integer | Primary key             |
| child_id | Integer | Foreign key to Children |
| date     | Date    | Attendance date         |
| status   | String  | Attendance status       |

### Enrollment

| Field    | Type    | Description             |
| -------- | ------- | ----------------------- |
| id       | Integer | Primary key             |
| child_id | Integer | Foreign key to Children |
| date     | Date    | Enrollment date         |

---

## Environment Variables

The following environment variables need to be set:

| Variable         | Description                       |
| ---------------- | --------------------------------- |
| `DATABASE_URL` | PostgreSQL database URL           |
| `SECRET_KEY`   | Secret key for JWT authentication |

---

## Running the Application

1. Set up the environment:

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
2. Run the Flask server:

   ```bash
   flask run
   ```

---

## API Documentation

You can view the API documentation using **Swagger UI** by navigating to:



---
## Frontend Overview

The frontend of this project is built using **React** with **React Router** for navigation between different pages. The key routes and components in the application include:

### Routes and Components

- **/register**: Renders the `Register` component for user registration.
- **/login**: Renders the `Login` component for user login.
- **/children**: Displays the `ChildList` component, showing a list of children.
- **/add-child**: Renders the `AddChild` component to allow adding a new child.
- **/caregivers**: Displays the `CaregiverList` component, showing a list of caregivers.
- **/**: Defaults to the `Register` component.

### Core Components Used

1. **Navbar**: A common navigation bar for the entire application.
2. **Register**: Handles user registration.
3. **Login**: Manages user authentication and JWT retrieval.
4. **ChildList**: Fetches and displays the list of children from the backend.
5. **AddChild**: A form to add a new child to the system.
6. **CaregiverList**: Displays the caregivers associated with children.
---
## How to Run the Frontend

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   npm install
   npm start
   ```
