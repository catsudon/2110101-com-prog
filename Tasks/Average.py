sum = 0
cnt = 0
while(True):

    a = input()
    if(a == "q"):
        break
    sum+=float(a)
    cnt+=1

if(cnt == 0):
    print("No Data")
else:
    print(round(sum/float(cnt), 2))