from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import datetime
import random
import uvicorn

app = FastAPI(title="Video Camera API", version="1.0.0")


def generate_random_status() -> str:
    """Generate random status from: good, bad, normal"""
    return random.choice(["good", "bad", "normal"])


@app.get("/videocamera")
async def get_videocamera_status(location: str = Query(..., description="Location name")):
    """
    Get video camera status by location.
    Returns random status (good/bad/normal) for the specified location.
    """
    status = generate_random_status()
    
    response = {
        "status": status,
        "location": location,
        "timestamp": datetime.now().isoformat(),
        "description": f"Video camera status for {location}: {status}"
    }
    
    return JSONResponse(content=response)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)

