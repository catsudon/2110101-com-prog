
# Task: ZigZag_2.py

``` py
cmd = ""
a,b= [],[]
toggle = True
while(1):
    cmd = input()
    try:
        x,y = (int(i) for i in cmd.split())
        if(toggle): a+=[x];b+=[y]
        else: b+=[x];a+=[y]
        toggle = not toggle
    except Exception:break

print(a,b)

if(cmd == "Zig-Zag"): print(min(a), max(b))
else: print(min(b), max(a))
```
    