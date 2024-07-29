N, T = map(int, input().split())
#print(N)
#print(T)
deliveries = []
for i in range(N):
    d = tuple(map(int, input().split()))
    deliveries.append(d)
#print(deliveries)
deliveries += [(T + 1, 0)]

remaining, total,last_d = 0,0,0
for day, haybale in deliveries:
    total += haybale
    remaining -= day - last_d
    last_d = day
    remaining = max(remaining, 0) + haybale


print(total - remaining)
