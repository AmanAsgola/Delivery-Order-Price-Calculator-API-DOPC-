# Delivery Order Price Calculator API (DOPC)

## Overview
The **Delivery Order Price Calculator API (DOPC)** is a backend service that calculates the total price for a delivery order, including small order surcharges and delivery fees, based on real-time venue and user location data. This project was developed as part of Wolt's Backend Engineering Internship assignment.

## Features
- **REST API** with a single endpoint (`/api/v1/delivery-order-price`).
- Fetches **venue details** dynamically from Wolt's Home Assignment API.
- **Calculates delivery distance** using a straight-line approximation between the venue and user location.
- Computes **delivery fees** based on a distance-based pricing model.
- Implements **small order surcharge logic** for orders below the minimum threshold.
- Optimized for **performance with caching** and **asynchronous execution**.

## API Endpoint
### `GET /api/v1/delivery-order-price`
#### Query Parameters:
- `venue_slug` (string) - Unique identifier of the venue.
- `cart_value` (integer) - Total value of items in cents.
- `user_lat` (float) - User's latitude.
- `user_lon` (float) - User's longitude.

#### Example Request:
```bash
curl http://localhost:8000/api/v1/delivery-order-price?venue_slug=home-assignment-venue-berlin&cart_value=1200&user_lat=52.5200&user_lon=13.4050
```

#### Example Response:
```json
{
  "total_price": 1390,
  "small_order_surcharge": 0,
  "cart_value": 1200,
  "delivery": {
    "fee": 190,
    "distance": 500
  }
}
```

## Technologies Used
- **Backend Framework**: FastAPI (Python)
- **API Integration**: Requests
- **Mathematical Computation**: Haversine formula (for distance calculation)
- **Performance Optimization**: AsyncIO, Caching
- **Testing**: Pytest, Unit Tests
- **Containerization**: Docker (optional)

## Installation & Running Instructions
### Prerequisites:
- Python 3.8+
- Virtual environment (recommended)
- `pip install -r requirements.txt`

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/AmanAsgola/dopc-api.git
   cd dopc-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
4. Open API documentation in browser:
   ```
   http://localhost:8000/docs
   ```

## Testing
Run tests using:
```bash
pytest tests/
```

## Future Improvements
- Implement **rate limiting** for API requests.
- Add **geospatial optimization** for more accurate delivery distance calculation.
- Introduce **load balancing and caching strategies** for enhanced scalability.

## Contributors
Developed by **Aman Asgola** as part of Wolt's Backend Engineering Internship assignment.

---
Feel free to contribute or reach out for improvements!

