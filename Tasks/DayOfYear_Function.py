day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
quick_sum = [0 for i in range(13)]

def day_of_year(d, m, y):
    y-=543
    sum = quick_sum[m-1]
    sum+=d
    if y % 4 == 0 and y % 100 != 0 and sum > 60:
        sum+=1
    return sum

def main():
    for i in range(1,13):quick_sum[i]=quick_sum[i-1]+day_in_month[i]

main()
exec(input()) # DON'T remove this line