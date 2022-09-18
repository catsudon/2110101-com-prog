from functools import reduce

def make_int_list(x):
    if(not len(x)):return []
    return list(map(int, x.split(' ')))
 # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
 # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
def is_odd(e):
    return e%2==1
 # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
def odd_list(a_list):
    return list(filter(is_odd, a_list))
 # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
 # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
def sum_square(a_list):
    if(not len(a_list)):return 0
    return reduce(lambda sum,x : sum+x*x, a_list)
 # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
 # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
exec(input().strip())