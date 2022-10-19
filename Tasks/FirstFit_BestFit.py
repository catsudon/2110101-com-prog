def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    o=0
    for i in range(len(L)):
        if(100-sum(L[i]) >= e ):
            L[i] += [e]
            o=1;break
    if(not o):
        L+=[[e]]
    
    return L
            
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    o=0;best=-1;mx=0
    for i in range(len(L)):
        l = L[i]
        s = sum(l)
        if(100-s >= e and e+s > mx):
            best = i
            mx = e+s
            o=1
    if(o): L[best].append(e)
    else: L+=[[e]]
    
    return L

def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    ans = []
    for i in D: ans = first_fit(ans, i)
    return ans
        
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    ans = []
    for i in D: ans = best_fit(ans, i)
    return ans
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ