from dataclasses import dataclass
import random

### Helper Functions ###

@dataclass
class Order:
    type: str
    price: int
    volume: int
    mes: int = 0

    def __lt__(self, other):
        # price ascending then volume descenting
        if self.price == other.price:
            return self.volume < other.volume
        else:
            return self.price > other.price

def create_random_order():
    type = random.choice(['b', 's'])
    vol = 1#random.choice(range(1,100))
    price = random.choice(range(1,100))
    mes = random.choice(range(vol+1))
    return Order(type, price, vol)# mes)

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
