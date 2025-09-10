n,t = list(map(int,input().split()))
queue= list(input())

for i in range(t):
  for j in range(len(queue)-2,-1,-1):
    if queue[j+1] == "G" and queue[j] == "B":  # BG
      queue[j+1] = "B"
      queue[j] = "G"

print("".join(queue))

#BGGBG

#GGBGB