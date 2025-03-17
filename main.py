from fastapi import FastAPI, HTTPException, Query
from services import calculate_delivery_order_price
from pydantic import ValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/v1/delivery-order-price")

def delivery_order_price(
    venue_slug: str = Query(..., description="Unique identifier for the venue"),
    cart_val: int = Query(..., ge=0, description="Total value of items in cents"),
    user_lat: float = Query(..., description="Latitude of user location"),
    user_lon: float = Query(..., description="Longitude of user location")):

    VENUE_SLUG_MAPPING = {
    "berlin": "home-assignment-venue-berlin",
    "helsinki": "home-assignment-venue-helsinki",
    "stockholm": "home-assignment-venue-stockholm",
    "tokyo": "home-assignment-venue-tokyo"}
    
    if venue_slug in VENUE_SLUG_MAPPING:
        venue_slug = (VENUE_SLUG_MAPPING[venue_slug])
    


    try:
        return calculate_delivery_order_price(venue_slug, cart_val, user_lat, user_lon)
    except ValidationError as e:
        raise HTTPException(status_code=423, detail=str(e))
    except Exception as e:
        raise JSONResponse(status_code=502,content={"detail": f"An error occurred: {str(e)}"})