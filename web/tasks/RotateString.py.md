
# Task: RotateString.py

``` py
mode = input().strip()
dimension = int(input())
a = []

l = 0;st = 1

for i in '1'*dimension:
    r = input().strip()
    if(st):l=len(r)
    if(len(r) != l):
        print("Invalid size")
        exit()
    a+=[r];st=0


if(mode == '180'):
    a.reverse()
    for i, st in enumerate(a):
        a[i] = st[::-1]

if(mode == 'flip'):
    for i, st in enumerate(a):
        a[i] = st[::-1]

if(mode == '90'):
    b = ['' for i in '1'*max(len(a),len(a[0]))]
    for i in reversed(a):
        cnt = 0
        for j in i:
            b[cnt]+=j
            cnt+=1
    a=b

for i in a:print(i)
```
    