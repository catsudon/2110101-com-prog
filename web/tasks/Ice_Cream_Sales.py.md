
# Task: Ice_Cream_Sales.py

``` py
sales = {}
menu = {}
# !!!! don't assign it as ```sales = menu = {}``` 
# dictionary is passed by reference
total = 0

n = int(input())
for i in range(n):
    name, price = input().split()
    menu[name] = float(price)


q = int(input())
for i in '*'*q:
    name, quantity = input().split()
    quantity = float(quantity)
    try:
        price=menu[name]
       # print("debug",quantity, price ,quantity*price)
    except Exception:
        continue
    
    try:
        sales[name] += quantity*price
    except Exception:
        sales[name]  = quantity*price
    
    total += quantity*price

mx = [] 
for key in sales:
    money = sales[key]
    mx += [(-money,key)]

mx.sort()
st = True
dp = 0
brand = []
for i in range(len(mx)):
    sale = -mx[i][0]
    name = mx[i][1]
    if(st):
        brand += [name]
        dp = sale
        st = 0
    elif(sale == dp): brand += [name]
        
if(not len(brand)):
    print("No ice cream sales")
else:
    print("Total ice cream sales: {}".format(total))
    print("Top sales: {}".format(", ".join(brand)))
```
    