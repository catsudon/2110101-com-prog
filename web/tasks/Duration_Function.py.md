
# Task: Duration_Function.py

``` py
def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]), int(t[1]), int(t[2])


def hms2str(h, m, s):
    return ('0'+str(h))[-2:] + ':' + \
        ('0'+str(m))[-2:] + ':' + \
        ('0'+str(s))[-2:]


def to_sec(h, m, s):
    return h*60*60 + m*60 + s


def to_hms(s):
    return tuple(map(int, ((s/60)/60,(s/60)%60,s%60)))


def diff(h1, m1, s1, h2, m2, s2):
    t1 = to_sec(h1, m1, s1)
    t2 = to_sec(h2, m2, s2)
    diff = t2-t1
    return to_hms(diff)


def main():
    hms_start = input()
    hms_end = input()
    t1 = map(int, tuple(hms_start.split(':')))
    t2 = map(int, tuple(hms_end.split(':')))
    print(hms2str(*diff(*t1,*t2)))

exec(input())  # DON'T remove this line
```
    