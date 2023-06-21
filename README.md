# Energy Expenditure API

The Energy Expenditure API is a FastAPI-based application that provides endpoints for checking the health of the API and
predicting energy expenditure based on a specified model. The prediction endpoint accepts input data points and uses a
specified model to estimate energy expenditure, returning a fake prediction for now.

## API Endpoints

- GET `/health`: Check health of the API
- POST `/predict`: Predict energy expenditure estimation using a specified model.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/energy-expenditure-api.git
```

2. Navigate to the project directory:

```bash
cd energy-expenditure-api
```

### Build and Run the Application

```bash
docker-compose up --build
```

The API should now be running at http://localhost:80.
Visit http://localhost:8080 for accessing the API.


