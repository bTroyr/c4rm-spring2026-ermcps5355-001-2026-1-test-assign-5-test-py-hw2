def getBondDuration(y, face, couponRate, m, ppy = 1):

    rate_per_period = y / ppy          
    coupon_per_period = face * couponRate / ppy  
    total_periods = m * ppy          
    total_pvcf = 0.0                
    weighted_pvcf = 0.0             
    
    for period in range(1, total_periods + 1):
        if period < total_periods:
            cash_flow = coupon_per_period
        else:
            cash_flow = coupon_per_period + face
        
        pvcf = cash_flow / (1 + rate_per_period) ** period
        
        total_pvcf += pvcf
        weighted_pvcf += pvcf * period
    
    duration = weighted_pvcf / total_pvcf
    
    return(duration)
