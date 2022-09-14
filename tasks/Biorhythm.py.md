
# Task: Biorhythm.py

``` py
from math import sin, pi

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
quick_sum = [0 for i in range(13)]
for i in range(1,13):quick_sum[i]=quick_sum[i-1]+day_in_month[i]

bd, bm, by, d, m, y = [int(e) for e in input().split()]

by -= 543
y -= 543

red = quick_sum[12] - quick_sum[bm]
red += (day_in_month[bm] - bd) + 1
if(by%4==0 and by%100!=0 and bm <= 2):red+=1

black = 365*(y-by-1)

blue = quick_sum[m-1]
blue += d - 1
if(y%4==0 and y%100!=0 and m > 2):blue+=1

t = red+black+blue
phy = sin((2*pi*t)/23)
emo = sin((2*pi*t)/28)
intt = sin((2*pi*t)/33)

print("{} {:.2f} {:.2f} {:.2f}".format(t, phy, emo, intt))
```
    