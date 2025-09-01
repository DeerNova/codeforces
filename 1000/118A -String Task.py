st = input().lower()
vowel = ["A", "O", "Y", "E", "U", "I"]
new = ""
for ch in st :
  if ch in vowel :
    pass
  else :
    ch = "."+ ch 
    new = new + ch  

print(new)