from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.crop_agent import generate_advisory

app = FastAPI(title="AI Smart Crop Advisory")

class AdvisoryRequest(BaseModel):
    crop: str
    location: str
    soil_type: str
    goal: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/api/advisory")
async def get_advisory(data: AdvisoryRequest):
    try:
        prompt = f"""
Crop: {data.crop}
Location: {data.location}
Soil Type: {data.soil_type}
Goal: {data.goal}
"""
        return {"advisory": await generate_advisory(prompt)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
