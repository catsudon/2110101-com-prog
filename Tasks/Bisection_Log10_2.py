def check(a, powed):
    diff = a-powed
    if(abs(diff) <= 0.0000000001):
        return True

    return False


a = float(input())
ta = a
ans = 0
L,U = 0,0
while(ta > 0):
    ta//=10
    U+=1

oldmid=-1
while(L <= U):
    mid = (L+U)/2
    r = 10**mid
    ck = check(a, r)
    #print("debug ", mid)
    if(ck == True or oldmid==mid):
        print(round(mid, 6))
        break
    elif(r < a):
        L = mid
    else:
        U = mid
    oldmid=mid
