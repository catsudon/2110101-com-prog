
# Task: UniqueCount.py

``` py
a = list(map(int, input().split()))
a.sort()
pre = 99999999

cnt = 0 
array = []
for cur in a:
    if(cur==pre):continue
    if(len(array) < 10):array.append(int(cur))
    cnt+=1
    pre = cur

print(cnt)
print(array)
```
    