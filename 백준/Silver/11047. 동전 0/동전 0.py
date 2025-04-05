import sys

N, K = map(int, sys.stdin.readline().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

min = 0

for coin in coins:
    if K >= coin:
        min += K//coin
        K %= coin
        if K <= 0:
            break

print(min)