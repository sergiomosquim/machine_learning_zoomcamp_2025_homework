from fastapi import FastAPI
import uvicorn
import pickle
from typing import Literal
from pydantic import BaseModel, PositiveInt, PositiveFloat, ConfigDict

app = FastAPI(title = 'lead_score')

class Client(BaseModel):
    model_config = ConfigDict(extra="forbid")
    lead_source: Literal["organic_search", "social_media", "paid_ads", "referral", "events"]
    number_of_courses_viewed: PositiveInt
    annual_income: PositiveFloat

class PredictResponse(BaseModel):
    prob_susbcription: float
    subscription: bool

with open('pipeline_v2.bin', mode='rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(client):
    res = pipeline.predict_proba(client)[0,1]
    return float(res)

@app.post("/predict")
def predict(client: Client) -> PredictResponse:
    prob = predict_single(client.model_dump())
    return PredictResponse(
        prob_susbcription=prob,
        subscription=prob >= 0.5
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 9696)