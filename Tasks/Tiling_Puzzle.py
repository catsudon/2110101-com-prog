def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        for j in t[i]:
            if e == j:
                return i
            
def flatten(t): # return a list of ints converted from list of lists of ints t
    a = []
    for i in t:
        for j in i:
            if j != 0:
                a+=[j]
    return a

def inversions(x): # return the number of inversions of list x
    cnt=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if(x[i] > x[j]):cnt+=1
    return cnt
def solvable(t): # return True if tiling t (list of lists of ints) is solvable
 # otherwise return False
    llenn = len(t)
    flat = flatten(t)
    inver = inversions(flat)
    if(llenn % 2 == 1 and inver % 2 == 0): return True
    if(llenn % 2 == 0):
        if(inver % 2 == 1):
            if(row_number(t, 0) % 2 == 0): return True
        else:
            if(row_number(t, 0) % 2 == 1): return True
    
    return False
 
 
exec(input().strip()) # do not remove this line
