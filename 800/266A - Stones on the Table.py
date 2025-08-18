
n = int(input())
s = input()

count_removed = 0 
for index in range(len(s)-1) : #RRG
  if s[index+1] == s[index] :
    count_removed += 1
print(count_removed)
