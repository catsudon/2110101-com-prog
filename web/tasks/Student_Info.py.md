
# Task: Student_Info.py

``` py
n = int(input())
g2n = {}
y2n = {}
d2n = {}
n2data = {}
namelist = set()
for i in range(n):
    name, group, year, depart = input().split(' ')
    namelist.add(name)
    n2data[name] = [name,group,year,depart]
    try: g2n[group].add(name)
    except: g2n[group] = set([name])
    
    try: y2n[year].add(name)
    except: y2n[year] = set([name])
    
    try: d2n[depart].add(name)
    except: d2n[depart] = set([name])

g = y = d = False
gs = set()
ys = set()
ds = set()
filt = input().split()
for i in filt:
    if((len(i) == 1 or i == 'Dog') and not i.isdigit()):
        g = 1
        try:
            for name in g2n[i]:
                gs.add(name)
        except: g=0
        
    elif(i.isdigit()):
        y = 1
        try:
            for name in y2n[i]:
                ys.add(name)
        except: y=0
    else:
        d = 1
        try:
            for name in d2n[i]:
                ds.add(name)
        except: d=0

ans = namelist
if(g): ans = ans.intersection(gs)
if(y): ans = ans.intersection(ys)
if(d): ans = ans.intersection(ds)
ans = list(ans)
if(not (g or y or d)):
    ans = []
ans.sort()
for i in ans:
    print((" ").join(n2data[i]))
if(len(ans)==0): print("Not Found")
```
    