from dataclasses import dataclass
import random

### Helper Functions ###

@dataclass
class Order:
    client: bytes = ''
    type: str = ''
    asset: str = ''
    price: int = 0
    volume: int = 1
    mes: int = 0

    def copy(self):
        return Order(self.client, self.type, self.asset, self.price,
                     self.volume, self.mes)

def create_random_order():
    type = random.choice(['b', 's'])
    price = random.choice(range(1,100))
    return Order(type = type, price = price)

### Maximizing Matching Functions ###

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
