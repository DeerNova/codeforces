# 512 = 2 + 1 * 10 + 5 * 100 = 2 + 10*(1+50)
n , k = list(map(int,input().split()))

for i in range(k):
  last_digit = n % 10
  if last_digit == 0 :
    n = n // 10
  else :
    n = n - 1
  
print(n)