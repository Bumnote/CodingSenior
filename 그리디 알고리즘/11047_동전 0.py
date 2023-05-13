from sys import stdin

input = stdin.readline

# 변수 입력 부분 #
n, k = map(int, input().split())  # n: 동전의 종류 / k: 동전의 가치 합
coins = [int(input().strip()) for _ in range(n)]

# 문제 해결 부분 #
total_coin = 0
for i in range(len(coins) - 1, -1, -1):
    if coins[i] > k:
        continue
    total_coin += k // coins[i]
    k %= coins[i]
    if k == 0:
        print(total_coin)
        break
