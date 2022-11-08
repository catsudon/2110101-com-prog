
# Task: Bidding.py

``` py
q = int(input())
b = {};w = {}
manlist = set()

for Q in range(q):
    cmd = input().split(' ')
    if (cmd[0] == 'B'):
        man, obj, price = cmd[1:]
        manlist.add(man)
        price = - int(price)
        if (obj in b):
            b[obj] += [(price, Q, man)]
        else:
            b[obj] = [(price, Q, man)]
    if (cmd[0] == 'W'):
        if (cmd[1],cmd[2]) in w: w[cmd[1],cmd[2]] += [Q]
        else: w[cmd[1],cmd[2]] = [Q]
ans = {}
for key, val in b.items():
    l = sorted(val)
    for i in l:
        price, queue, man = i
        price=-price
        k = (man,key)
        f = 0
        if(k in w):
            for q in w[k]:
                if q > queue:
                    f = 1
        if f: continue
        if(man in ans):
            ans[man][0]+=price
            ans[man][1]+=[key]
        else: ans[man] = [price,[key]] 
        break

# print(ans)
for name in sorted(manlist):
    riru = name+": $"
    if name in ans:
        price,items = ans[name]
    else: price,items = 0,[]
    riru += str(price)
    if(len(items)): 
        riru += " -> " + " ".join(sorted(items))    
    print(riru)
```
    