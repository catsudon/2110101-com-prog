def print_triangle(h):
    a=h-1
    b=1
    for i in range(1,h+1):
        if(i==1 or i==h):print(" "*a+"*"*(i*2-1))
        else:print(" "*a+"*"+" "*b+"*");b+=2
        a-=1
        
exec(input())