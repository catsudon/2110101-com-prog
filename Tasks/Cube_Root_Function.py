from math import sqrt

def sqrt_n_times(x, n):
    for i in range(n):
        x=sqrt(x)
    return x
def cube_root(y):
 # คืนค่าประมาณของรากที่สามของ y โดยใชวิธี ้ ที่เสมือนการกดปุ่มด้วยสูตร
 # 
 # ข้อแนะน า: เรียกใชฟ้ ังกช์ ัน sqrt_n_times
 exp = (1/(2**2)) * (1 + 1/(2**2)) * (1 + 1/(2**4)) * (1 + 1/(2**8)) * (1 + 1/(2**16))* (1 + 1/(2**32))  
 return(y**exp)
def main():
 q = float(input())
 print(cube_root(q))
exec(input()) # DON'T remove this line