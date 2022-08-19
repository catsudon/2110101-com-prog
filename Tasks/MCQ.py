a = input()
b = input()

score=0
for i in range(len(a)):
    try:
        if(a[i]==b[i]):score+=1
    except Exception:
        score=-69696969

if(score<0):print("Incomplete answer")
else:print(score)