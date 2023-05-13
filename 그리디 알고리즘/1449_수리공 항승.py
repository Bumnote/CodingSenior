from sys import stdin
input = stdin.readline

# 변수 입력 부분 #
n, l = map(int, input().split())  # n: 물이 새는 곳의 개수 / l: 테이프의 길이
water_leak = list(map(int, input().split()))
taping = [False for _ in range(n)]
tape = []
total_tape = 0

# 문제 해결 부분 #
water_leak.sort()
for leak_loc in water_leak:
    tape.append((leak_loc - 0.5, leak_loc + 0.5))

for i in range(n):
    if not taping[i]:
        total_tape += 1
        taping[i] = True
    else:
        continue
    for j in range(i + 1, n):
        if tape[j][1] - tape[i][0] <= l:
            taping[j] = True
        else:
            break

print(total_tape)

"""
N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True 
    
ans = 0 
x = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)
"""