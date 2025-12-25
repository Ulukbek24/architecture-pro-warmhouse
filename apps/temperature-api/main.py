from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from datetime import datetime
import random
import uvicorn

app = FastAPI(title="Temperature API", version="1.0.0")


def get_location_by_sensor_id(sensor_id: str) -> str:
    """Get location based on sensor ID"""
    location_map = {
        "1": "Living Room",
        "2": "Bedroom",
        "3": "Kitchen"
    }
    return location_map.get(sensor_id, "Unknown")


def get_sensor_id_by_location(location: str) -> str:
    """Get sensor ID based on location"""
    sensor_map = {
        "Living Room": "1",
        "Bedroom": "2",
        "Kitchen": "3"
    }
    return sensor_map.get(location, "0")


def generate_random_temperature() -> float:
    """Generate random temperature value between 18 and 25 degrees Celsius"""
    return round(random.uniform(18.0, 25.0), 1)


@app.get("/temperature")
async def get_temperature(location: str = Query(..., description="Location name")):
    """
    Get temperature by location.
    Returns random temperature value for the specified location.
    """
    # Generate sensor ID based on location
    sensor_id = get_sensor_id_by_location(location)
    
    # Generate random temperature
    temperature_value = generate_random_temperature()
    
    response = {
        "value": temperature_value,
        "unit": "°C",
        "timestamp": datetime.now().isoformat(),
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature reading for {location}"
    }
    
    return JSONResponse(content=response)


@app.get("/temperature/{sensor_id}")
async def get_temperature_by_id(sensor_id: str):
    """
    Get temperature by sensor ID.
    Returns random temperature value for the sensor with specified ID.
    """
    # Get location based on sensor ID
    location = get_location_by_sensor_id(sensor_id)
    
    # Generate random temperature
    temperature_value = generate_random_temperature()
    
    response = {
        "value": temperature_value,
        "unit": "°C",
        "timestamp": datetime.now().isoformat(),
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": f"Temperature reading for sensor {sensor_id} at {location}"
    }
    
    return JSONResponse(content=response)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={"status": "ok"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

