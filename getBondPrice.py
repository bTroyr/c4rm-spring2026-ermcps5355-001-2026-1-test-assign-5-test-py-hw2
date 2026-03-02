def getBondPrice(y, face, couponRate, m, ppy=1):

    N = int(round(m * ppy)) 
    per_rate = y / ppy       
    coupon_per_period = face * couponRate / ppy 

    if N == 0:
        return float(face)

    if per_rate == 0:
        pv_coupons = coupon_per_period * N
        pv_face = face
    else:
        discount_factor_N = (1.0 + per_rate) ** (-N)
        annuity_factor = (1.0 - discount_factor_N) / per_rate
        pv_coupons = coupon_per_period * annuity_factor
        pv_face = face * discount_factor_N

    price = pv_coupons + pv_face
    return float(price)