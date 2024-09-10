import sys

sys.stdin=open('cow.in', 'r')
sys.stdout=open('cow.out', 'w')

N = int(input())
# print(N)
phrase = input()

C, O, W = 0, 0, 0
for i in range(N):
    ltr = phrase[i]
    if ltr == 'C':
        C+=1
    if ltr == 'O':
        O+=C
    if ltr == 'W':
        W+=O
print(W)
