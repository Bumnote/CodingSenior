from sys import stdin
from collections import deque

input = stdin.readline

n = int(input().strip())
dq = deque([ i for i in range(1, n + 1)])

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])