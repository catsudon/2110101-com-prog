
# Task: Bowling.py

``` py
a = input() + '0'*10
b = int(input())

mp = {'X':10}
for i in range(0,10):
    mp[str(i)]=i
haj = True
score = cur = cnt = 0
streak = idx = 0
c = -1
for i in a:
    if(haj):cnt+=1;cur=0
    haj=False

    if(cnt>10):break

    if(i.isdigit()): cur+=int(i);streak+=1
    if(i=='/'): 
        cur=10
        streak=2
        if(a[idx+1] == 'X'):cur+=10
        else:cur+=mp[a[idx+1]]
    if(i=='X'):
        cur=10
        streak=2
        if(a[idx+2] == '/'):cur+=10
        elif(a[idx+2] == 'X'):cur+=10;cur+=mp[a[idx+1]]
        else:cur+=mp[a[idx+1]]+mp[a[idx+2]]
    


    if(streak == 2): 
        streak = 0
        haj = True ; score += cur
        if(cnt == b):c=cur
        # print(cur)
    idx+=1

if(c != -1):print(c)
else:print(score)
```
    