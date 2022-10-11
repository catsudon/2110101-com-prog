def pay(pocket, amt):
    available = reversed(sorted(pocket.keys()))
    clone = pocket.copy()
    paid = {}

    for k in available:
        while amt >= k and clone[k] > 0:
            clone[k] -= 1
            if(k in paid): paid[k]+=1
            else: paid[k]=1
            amt -= k

    if amt != 0: return {}

    for k, v in clone.items():
        pocket[k] = v
    return paid