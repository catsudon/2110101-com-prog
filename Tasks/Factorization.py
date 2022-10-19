def factor(N):
    ans = []
    a = N
    for i in range(2,N+1):
        coef = 0
        while(a%i==0):
            a/=i
            coef+=1
        if(coef):ans+=[[i,coef]]
    return ans
exec(input().strip())