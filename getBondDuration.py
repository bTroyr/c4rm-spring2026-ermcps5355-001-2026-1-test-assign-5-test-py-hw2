def getBondDuration(y, face, couponRate, m, ppy=1):
    periodic_yield = y / ppy
    periodic_coupon = (face * couponRate) / ppy
    total_periods = m * ppy
    
    t = np.arange(1, total_periods + 1)
    
    cf = np.full(total_periods, periodic_coupon)
    cf[-1] += face
    
    pvcf = cf / (1 + periodic_yield)**t 
    bond_price = np.sum(pvcf)
    w = pvcf / bond_price
    duration = np.sum(w * t) / ppy
    
    return duration
