
# Task: Location_Analysis.py

``` py
n = int(input())
vst = {}
idx2town = {}
idx2prior = {} ; x=1
for i in range(n):
    a = input()
    idx, visits = a.split(': ')
    visits = visits.split(", ")
    idx2town[idx] = visits
    idx2prior[idx] = x; x+=1
    for visited_town in visits:
        try: vst[visited_town].add(idx)
        except: vst[visited_town] = set([idx]) 

idx = input()
ans = set()
for town in idx2town[idx]:
    for i in vst[town]:
        ans.add(i)

ans.remove(idx)
if(len(ans) == 0 ): print("Not Found")
finans = []
for i in ans: finans += [(idx2prior[i], i)]
finans.sort()
for i  in finans: print(i[1])
```
    