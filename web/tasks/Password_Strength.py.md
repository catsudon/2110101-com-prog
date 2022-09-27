
# Task: Password_Strength.py

``` py
a = input().strip()
ok=1

if(len(a) < 8 ):
    print("Less than 8 characters")
    ok=0

if(a==a.upper()):
    print("No lowercase letters")
    ok=0

if(a==a.lower()):
    print("No uppercase letters")
    ok=0

found_digit = 0
for i in a:
    if(i.isdigit()):found_digit=1
if(not found_digit):
    print("No numbers")
    ok=0

found_symbol = 0
for i in a:
    if(not i.isdigit() and (i == i.lower()) and (i == i.upper())):found_symbol=1
if(not found_symbol):
    print("No symbols")
    ok=0

streak=mx=0
dp='あ'
for i in a.lower():
    if(dp==i):
        streak+=1
    else:
        streak=1
    mx = max(mx,streak)
    dp=i

if(mx >= 4 ):
    print("Character repetition")
    ok=0

streak=mx=dp=0
for i in a:
    if(dp+1==ord(i) and i.isdigit()):streak+=1
    else:streak=1
    mx = max(mx,streak);dp=ord(i)
streak=dp=0
for i in a:
    if(dp-1==ord(i) and i.isdigit()):streak+=1
    else:streak=1
    mx = max(mx,streak);dp=ord(i)

if(mx >= 4 or '0987' in a):
    print("Number sequence")
    ok=0

streak=mx=dp=0
for i in a.lower():
    if(dp+1==ord(i) and (i.upper() != i)):streak+=1
    else:streak=1
    mx = max(mx,streak);dp=ord(i)
streak=dp=0
for i in (a.lower()):
    if(dp-1==ord(i) and (i.upper() != i)):streak+=1
    else:streak=1
    mx = max(mx,streak);dp=ord(i)
if(mx >= 4 ):
    print("Letter sequence")
    ok=0

seq = ["qwertyuiop", 'asdfghjkl', 'zxcvbnm', '!@#$%^&*()_+']
for i in range(4,len(a)+1):
    check=a[i-4:i].lower()
    for j in seq:
        if(check in j or check in j[::-1]):
            print("Keyboard pattern")
            ok=0
            exit()

if(ok):print("OK")
```
    