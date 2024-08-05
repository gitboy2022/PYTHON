N = int(input())

def check_moo(s):
  for i in range(len(s)):
    if s[i:i + 3] == "MOO":
      return len(s) - 3
  for i in range(len(s)):
    if s[i:i + 3] == "MOM":
      return len(s) - 2
    if s[i:i + 3] == "OOO":
      return len(s) - 2
  for i in range(len(s)):
    if s[i:i + 3] == "OOM":
      return len(s) - 1
  return -1
    

for i in range(N):
  s = input()
  print(check_moo(s))
  
