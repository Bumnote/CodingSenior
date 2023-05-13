from sys import stdin
from itertools import combinations

input = stdin.readline

# 변수 입력 부분 #
heights = [int(input().strip()) for _ in range(9)]

# 문제 해결 부분 #
for height in combinations(heights, 7):
    if sum(height) == 100:
        print(*sorted(height), sep='\n')
        break
