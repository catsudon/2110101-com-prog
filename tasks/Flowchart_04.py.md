
# Task: Flowchart_04.py

``` py
x1 = input()
x2 = input()
x3 = input()
x = x1+x2+x3
x = x.strip()

if(len(x) != 9 ):
    print("ERROR")
    exit()

win = "-"
i = 0

interval = 1
while(i < 3 and win == "-"):
    if(x[3*i] == x[3*i+1] == x[3*i+2]):
        win = x[3*i]
    elif(x[i] == x[i+3] == x[i+6]):
        win = x[i]
    else:
        i+=1
    interval += 1
    if(interval == 9):
        break

if(win == "-"):
    if(x[0] == x[4] == x[8]):
        win = x[0]
    if(x[3] == x[4] == x[6]):
        win = x[6]

if(win == "-"):
    print("???")
else:
    print(win)
```
    