from math import sqrt, pi

def distance1(x1, y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return sqrt(dx**2+dy**2)
 
def distance2(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return sqrt(dx**2+dy**2)
 
def distance3(c1, c2):
    x1,y1,r1 = c1
    x2,y2,r2 = c2
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    ptago = sqrt(dx**2+dy**2)
    if(ptago <= r1+r2):
        overlap = True
    else:
        overlap = False
    return (ptago, overlap)
 
def perimeter(points):
    pre = points[0]
    sum = 0
    points += [pre]
    for i in points[1:]:
        sum+=distance2(pre,i) 
        pre = i
    return sum

exec(input().strip()) 