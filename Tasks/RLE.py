cmd = input()

def str2RLE():
    a = input()
    a+="あ"
    RLE = []
    curr = ''
    streak = 0
    for i in a:
        if(i==curr):streak+=1
        else:RLE.append((streak, curr));streak=1;curr=i
    ans=""
    for (cnt, char) in RLE:
        if(cnt==0):continue
        ans+="{} {} ".format(char, str(cnt))
    print(ans)

def RLE2str():
    ans=""
    a = input()
    a = a.split()
    for i in range(0,len(a),2):
        ans += a[i]*int(a[i+1])
    print(ans)

if(cmd == "str2RLE"):str2RLE()
elif(cmd == "RLE2str"):RLE2str()
else:print("Error")