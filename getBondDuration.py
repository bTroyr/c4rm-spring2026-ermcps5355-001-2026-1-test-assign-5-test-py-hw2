def getBondDuration(y, face, couponRate, m, ppy=1):
    N = int(round(m * ppy))
    if N == 0:
        return 0.0

    r = y / ppy
    c = face * couponRate / ppy

    if r == 0:
        price = c * N + face
        num = c * (N * (N + 1) / 2.0) + face * N
        return float((num / price) / ppy)

    v = 1.0 / (1.0 + r)
    vN = v ** N

    sum_v = v * (1.0 - vN) / (1.0 - v)
    price = c * sum_v + face * vN

    S1 = v * (1.0 - (N + 1.0) * vN + N * vN * v) / (1.0 - v) ** 2

    num = c * S1 + face * N * vN

    return float((num / price) / ppy)