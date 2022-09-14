
# Task: Decryption.py

``` py
msg = "🌟"+input()
a = 0 
b = 0

for i in range(4,33,7):
    a*=10
    a+=int(msg[i])

for i in range(8,33,5):
    b*=10
    b+=int(msg[i])

c = a + b + 10000
c = int(((c % 10000) - (c % 10)) / 10)#

csum = 0
for i in str(c):
    csum += int(i)

num = int(str(csum)[-1])
ch = chr(65 + num)

print('{}{}'.format(c, ch))
```
    