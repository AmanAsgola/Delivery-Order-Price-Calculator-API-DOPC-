import requests
from utils import calculate_distance,calculate_delivery_fee
from config import Base_static_url,Base_Dynamic_url

def calculate_delivery_order_price(venue_slug: str, cart_val: int, user_lat: float, user_lon: float):
    static_url= f"{Base_static_url}/{venue_slug}/static"
    Dynamic_url= f"{Base_Dynamic_url}/{venue_slug}/dynamic"
    # print(static_url)
    
    static_data=requests.get(static_url).json()
    Dynamic_data=requests.get(Dynamic_url).json()

    # feilds Extraction
    venue_coords=static_data['venue_raw']['location']['coordinates']
    mini_cart_val=Dynamic_data['venue_raw']['delivery_specs']['order_minimum_no_surcharge']
    base_price=Dynamic_data['venue_raw']['delivery_specs']['delivery_pricing']['base_price']
    dist_range=Dynamic_data['venue_raw']['delivery_specs']['delivery_pricing']['distance_ranges']

    # print(venue_coords)
    # print(mini_cart_val)
    # print(base_price)
    # for i in dist_range:
    #     print(i)
    '''testing'''
    # user_lat=24.93087
    # user_long=60.17094
    
    
    distance=calculate_distance(venue_coords[1],venue_coords[0],user_lat,user_lon)
    small_order_surcharge=max(0,mini_cart_val-cart_val)
    delivery_fee = calculate_delivery_fee(distance, base_price, dist_range)
    total_price=delivery_fee+cart_val+small_order_surcharge
    
    return {

        "total_price": total_price,
        "small_order_surcharge": small_order_surcharge,
        "cart_value": cart_val,
        "delivery": {
            "fee": delivery_fee,
            "distance": distance
        }
    }

# print(calculate_delivery_order_price('home-assignment-venue-helsinki',100,60.17094,24.93087))