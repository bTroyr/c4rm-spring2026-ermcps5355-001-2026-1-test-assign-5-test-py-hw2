def getBondPrice(y, face, couponRate, m, ppy=1):
   
    rate_per_period = y / ppy         
    coupon_per_period = face * couponRate / ppy  
    total_periods = m * ppy          
    
    bond_price = 0.0
    
    for period in range(1, total_periods + 1):
        if period < total_periods:
            cash_flow = coupon_per_period  
        else:
            cash_flow = coupon_per_period + face 
            
        pv = cash_flow / (1 + rate_per_period) ** period
        bond_price += pv
    
    return(bond_price)