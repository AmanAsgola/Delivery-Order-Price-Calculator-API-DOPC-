from pydantic import BaseModel

class DeliveryDetails(BaseModel):
    fee:int
    distance:int

class DeliveryOrderPriceResponse(BaseModel):
    total_price: int
    small_order_surcharge: int
    cart_value: int
    delivery: DeliveryDetails