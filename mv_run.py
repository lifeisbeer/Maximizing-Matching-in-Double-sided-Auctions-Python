from mv_matching import mv, create_random_order

client_num = 100
bids = []
asks = []
for i in range(client_num):
    order = create_random_order()
    #print(order)
    if order.type == 'b':
        bids.append(order)
    else:
        asks.append(order)
# sort by price then volume
bids.sort()
for b in bids:
    print(b)
asks.sort()
for a in asks:
    print(a)
matching = mv(bids, asks)
for i in range(len(matching)):
    print(i+1, matching[i])
