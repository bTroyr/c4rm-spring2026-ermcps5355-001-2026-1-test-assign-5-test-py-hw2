def getBondPrice(market_rate, face_value, coupon_rate, years, freq):
    periodic_rate = market_rate / freq
    total_periods = years * freq
    periodic_coupon = face_value * coupon_rate / freq
    
    if periodic_rate == 0:
        pv_annuity = total_periods * periodic_coupon
    else:
        pv_annuity = periodic_coupon * (1 - (1 + periodic_rate)**-total_periods) / periodic_rate

    pv_face = face_value / (1 + periodic_rate)**total_periods
    bond_price = pv_annuity + pv_face
    
    return bond_price