from datetime import datetime
from enum import Enum
from random import uniform
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


# Define your Enum
class DeviceType(str, Enum):
    E4 = "E4"
    MUSE = "MUSE"
    ZEPHYR = "ZEPHYR"
    EARBUDS = "EARBUDS"


# Define your DataPoint model
class DataPoint(BaseModel):
    timestamp: datetime
    device: DeviceType
    x: float
    y: float
    z: float


# Define your request body for the predict endpoint
class PredictRequest(BaseModel):
    model: str
    input: List[DataPoint]


# Define your response body for the predict endpoint
class PredictResponse(BaseModel):
    met: float
    confidence: float
    model: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "healthy"}


@app.get("/health")
def check_health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictResponse)
def predict_energy_expenditure(data: PredictRequest):
    # For now, we just return a fake prediction
    return {
        "met": uniform(1, 10),
        "confidence": uniform(0, 1),
        "model": data.model
    }
