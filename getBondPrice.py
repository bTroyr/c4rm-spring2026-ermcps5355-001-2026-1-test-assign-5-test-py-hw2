def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    c = (face * couponRate) / ppy
    n = m * ppy
    
    periods = np.arange(1, n + 1)
    
    coupon_pvs = c / (1 + r)**periods
    
    face_pv = face / (1 + r)**n
    
    bond_price = np.sum(coupon_pvs) + face_pv
    
    return bond_price