w_limak , w_bob = list(map(int,input().split()))

years = 0
# while w_limak  <= w_bob:  # while not w_limak > w_bob
#   w_limak = w_limak * 3
#   w_bob = w_bob * 2
#   years += 1

# print(years)

while True :
  if  w_limak  <= w_bob :  # if w_limak > w_bob:
                           # break
                           #  else :
    w_limak = w_limak * 3
    w_bob = w_bob * 2
    years += 1

  else :
    break


print(years)