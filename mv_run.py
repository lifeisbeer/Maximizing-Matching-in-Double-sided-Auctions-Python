from mv_matching import mv, create_random_order
from operator import attrgetter

client_num = 10
verbose = True

def main():
    bids = []
    asks = []
    for i in range(client_num):
        order = create_random_order()
        if verbose:
            print("Order:", order)

        if order.type == 'b':
            bids.append(order)
        else:
            asks.append(order)

    # sort in ascending price
    bids.sort(key=attrgetter("price"))
    asks.sort(key=attrgetter("price"))

    if verbose:
        for b in bids:
            print("Bid:", b)

        for a in asks:
            print("Ask:", a)

    matching = mv(bids, asks)
    for i in range(len(matching)):
        print(i+1, matching[i])

if __name__ == '__main__':
    main()
