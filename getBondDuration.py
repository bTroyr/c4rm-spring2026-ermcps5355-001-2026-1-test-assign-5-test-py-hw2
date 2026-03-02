def getBondDuration(market_rate, face_value, coupon_rate, years, freq):
    def get_bond_price(r, fv, cr, y, fr):
        pr = r / fr
        tp = y * fr
        pc = fv * cr / fr
        if pr == 0:
            pva = tp * pc
        else:
            pva = pc * (1 - (1 + pr)**-tp) / pr
        pvf = fv / (1 + pr)**tp
        return pva + pvf
    
    periodic_rate = market_rate / freq
    total_periods = years * freq
    periodic_coupon = face_value * coupon_rate / freq
    bond_price = get_bond_price(market_rate, face_value, coupon_rate, years, freq)
    
    if periodic_rate == 0:
        sum_t_cf = (total_periods * (total_periods + 1) / 2) * periodic_coupon + total_periods * face_value
        duration = sum_t_cf / (total_periods * periodic_coupon + face_value)
    else:
        annuity_part = periodic_coupon * (1 - (1 + periodic_rate)**-total_periods - total_periods * periodic_rate * (1 + periodic_rate)**-total_periods) / (periodic_rate**2)
        face_part = total_periods * face_value / (1 + periodic_rate)**total_periods
        duration = (annuity_part + face_part) / bond_price
        duration = duration / freq
    
    return duration