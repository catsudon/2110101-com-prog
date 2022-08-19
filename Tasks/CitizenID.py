def check_digit(n):
   sum=0
   for i in range(12):
      sum+=(13-i)*int(n[i])
   ans = (11 - (sum % 11) ) % 10
   return ans

exec(input())