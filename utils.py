import math
def calculate_distance(lat1,lon1,lat2,lon2):
    R = 6371e3  # Earth's radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    ans=round(R * c)
    return ans
    
def calculate_delivery_fee(distance, base_price, dist_range):
    for range_item in dist_range:
        if range_item['min']<=distance<range_item['max'] or range_item['max']==0:
            a=range_item['a']
            b=range_item['b']
            fee = base_price + a + round(b*distance/10)
            return fee
    return 0
# print(calculate_distance(60.17012143,24.92813512,60.17094,24.93087))