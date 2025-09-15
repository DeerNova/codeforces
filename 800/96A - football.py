s = input() # 1000000001

flag = False
for index in range(len(s)-7):
  if s[index+1] == s[index] and s[index+2]== s[index] and s[index+3] == s[index] and \
    s[index+4] == s[index] and  s[index+5] == s[index] and  s[index+6] == s[index]:
    flag = True

if flag :
  print("YES")

else : 
  print("NO")

flag = False
for index in range(len(s)-7):
  count = 0
  for j in range(index,index+7):
    if s[j] == s[index]:
      count += 1
    else :
      break
  if count >= 7:
   flag = True
   break

if flag :
  print("YES")

else : 
  print("NO")














flag = False
for index in range(len(s)-7):
  all_equal =True
  for j in range(index,index+7):
    if s[j] == s[index]:
      pass
    else :
      all_equal =False
      break
  if all_equal:
   flag = True
   break

if flag :
  print("YES")

else : 
  print("NO")






















# 3
count = 1    
flag = False
for index in range(len(s)-1):
  if s[index] == s[index+1]:
     count += 1
    
  else :
     count = 1

  if count >= 7 :
    flag = True
    break

if flag :
  print("YES")

else : 
  print("NO")

  