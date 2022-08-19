from math import pi,e,sqrt

def stirling(n):
    print((sqrt(2*pi)) * (n ** (n+1/2)) * (e ** (-n+(1/(12*n+1)))))
    print((sqrt(2*pi)) * (n ** (n+1/2)) * (e ** (-n+(1/(12*n)))))
    return n

n = input()
stirling(int(n))