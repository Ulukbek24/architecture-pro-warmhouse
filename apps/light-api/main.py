from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import datetime
import random
import uvicorn

app = FastAPI(title="Light API", version="1.0.0")


def generate_random_brightness() -> int:
    """Generate random brightness percentage between 0 and 100"""
    return random.randint(0, 100)


@app.get("/light")
async def get_light_status(location: str = Query(..., description="Location name")):
    """
    Get light brightness by location.
    Returns random brightness percentage (0-100) for the specified location.
    """
    brightness = generate_random_brightness()
    
    response = {
        "brightness": brightness,
        "unit": "%",
        "location": location,
        "timestamp": datetime.now().isoformat(),
        "description": f"Light brightness for {location}: {brightness}%"
    }
    
    return JSONResponse(content=response)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)

