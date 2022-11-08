
# Task: Spiral_Square.py

``` py
def spiral_square(n):  # n is a positive odd number
    a = [[0]*n for i in range(n)]
    co = n*n
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    direction = 0

    x, y = n-1, n-1
    while (co):
        a[x][y] = co
        co -= 1
        
        # print(print_square(a))
        
        tx = x+dx[direction]
        ty = y+dy[direction]
        
        if(tx < 0 or ty < 0 or tx >=n or ty >= n or a[tx][ty] != 0):
            direction += 1
            direction %= 4
            
        
        x += dx[direction]
        y += dy[direction]
            
    return a

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))


exec(input().strip())
```
    