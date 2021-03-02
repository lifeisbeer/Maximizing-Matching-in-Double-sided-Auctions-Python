def poll(lst):
    if lst:
        return lst.pop(0)
    else:
        return False

# bids and asks are ordered in ascending price
def find_max_vol(bids, asks):
    qmin = 0
    a = poll(asks)
    if a:
        b = poll(bids)
        while b and b.price < a.price:
            b = poll(bids)
        qd = 0
        q = 0
        while b:
            if a and a.price <= b.price:
                q = q + a.volume
                a = poll(asks)
            else:
                q = q - b.volume
                qmin = min(qmin, q)
                qd = qd + b.volume
                b = poll(bids)
        qmin = qmin + qd
    return qmin

# bids and asks are ordered in ascending price
def mv(bids, asks):
    q = find_max_vol(bids.copy(), asks.copy())
    print(q)
    m = []
    for i in range(q):
        r_pos = len(bids)-q+i
        m.append((bids[r_pos], asks[i]))
    return m
