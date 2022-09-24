
# Task: Sample_Quiz_1.py

``` py
def end(a,b,c):
    print(a,b,c)
    exit()


a = int(input())
b = int(input())
c = int(input())

looped = False
got_in_c1 = False

while((a<100 and not looped) or (looped and not a/(b*c) > 20)):
    looped = True
    got_in_c1 = True
    if(b < c):
        a+= b**2 + c**2
        if(a % 10 == 5):
            break
        else:
            if(a%2==0): b+=1
            else: c-=1

            if(a/(b*c) > 20):
                break
            else:
                continue
    else:
        break

if(not got_in_c1):
    if(a < b):
        if(b < c):
            a=a+3
            b=a+c
            c=b+a
            end(a,b,c)
        else:
            if(a<c):
                a*=2
                b+=a
                c+=b
                end(a,b,c)
            else:
                a+=c
                b*=2
                c=b-a
                end(a,b,c)
    else:
        if(c>a):
            a=3*b
            b=c+a
            c=a+b
            end(a,b,c)
        else:
            if(b>c):
                a=b+c
                b=7*a
                c=b-a
                end(a,b,c)
            else:
                a=c-5
                b=a-b
                c=3*b
                end(a,b,c)


print(a,b,c)
```
    