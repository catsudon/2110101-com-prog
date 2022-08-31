q = []
k = int(input())
wait_time,checked_out,number,callstack = 0,0,0,0
for i in k*'🌟':
    cmd = input().split()
    if(cmd[0] == 'reset')       :number = int(cmd[1])
    if(cmd[0] == 'new')         :print("ticket",number);t=cmd[1];q.append((number, int(t)));number+=1
    if(cmd[0] == 'next')        :print("call", q[0+callstack][0]);callstack+=1
    if(cmd[0] == 'order'):
        n,ti=q[0+callstack-1]
        for i in range(callstack):q.pop(0)
        print("qtime",n,int(cmd[1])-ti);wait_time+=int(cmd[1])-ti;checked_out+=1;callstack=0
    if(cmd[0] == 'avg_qtime')   :print("avg_qtime", round(wait_time/checked_out, 4))
