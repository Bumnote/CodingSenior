from sys import stdin
from collections import deque

input = stdin.readline

## 변수 입력 부분 ##
n, m = map(int, input().split())  # n: 유저 수, m: 친구 관계 수
vertex = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())  # v1 <-> v2
    vertex[v1].append(v2)
    vertex[v2].append(v1)


## 문제 해결 부분 ##
def bfs(x, y):
    deq = deque()
    deq.append((x, 0))
    visited[x] = False  # 방문 처리

    while deq:
        cur_x, cur_cnt = deq.popleft()
        if cur_x == y:
            return cur_cnt
        for next in vertex[cur_x]:
            # 방문할 수 있으면
            if visited[next]:
                visited[next] = False  # 방문 처리
                deq.append((next, cur_cnt + 1))


ans = 0
min_num = 5001
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if i != j:
            visited = [True] * (n + 1)
            total += bfs(i, j)
    if min_num > total:
        min_num = total
        ans = i

print(ans)
