import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m) * int(ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1, dtype=float)
    cf = np.full(n, c, dtype=float)
    cf[-1] = cf[-1] + face

    pv = cf / (1.0 + r) ** t
    price = pv.sum()

    dur_periods = (t * pv).sum() / price
    return dur_periods / ppy
