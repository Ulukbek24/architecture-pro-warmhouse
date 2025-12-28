from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import random
import uvicorn

app = FastAPI(title="Gate API", version="1.0.0")


def generate_random_state() -> str:
    """Generate random gate state: close or open"""
    return random.choice(["close", "open"])


@app.get("/gate")
async def get_gate_status():
    """
    Get gate status.
    Returns random state (close/open).
    """
    state = generate_random_state()
    
    response = {
        "state": state,
        "timestamp": datetime.now().isoformat(),
        "description": f"Gate is {state}"
    }
    
    return JSONResponse(content=response)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8084)

