# 1
# str = input()
# cnt1,cnt2,cnt3 = 0, 0,0
# for chr in str:
#   if chr == "1":
#     cnt1+=1
#   elif chr == "2":
#      cnt2+=1
#   elif chr == "3":
#      cnt3+=1


# arr = ["1"]*cnt1 + ["2"]*cnt2 +["3"]*cnt3
# print(arr)
# arr = []
# for i in range(cnt1):
#    arr.append("1")
# for i in range(cnt2):
#    arr.append("2")
# for i in range(cnt3):
#    arr.append("3")
# print(arr)
# print("+".join(arr))

# 2
# str = input()
# arr =[]
# for chr in str:
#   if chr != "+":
#     arr.append(chr)
# arr.sort()
# print(arr)
# print("+".join(arr))

# 3
arr = (sorted(list(input().split("+"))))
print("+".join(arr))


# x = list(input().split("+"))
# x.sort()



