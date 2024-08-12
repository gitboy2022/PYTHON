N, K = map(int, input().split(" "))
days = [int(x) for x in input().split(" ")]

total = 0
for i in range(N):
  if i == 0:
    total += K + 1
  else:
    extend_cost = days[i] - days[i - 1]
    sub_cost = K + 1
    cheapest = min(extend_cost, sub_cost)
    total += cheapest
print(total)
