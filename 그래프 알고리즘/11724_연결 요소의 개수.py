from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
input = stdin.readline

def dfs(num):
    visited[num] = True
    for elem in grid[num]:
        # 방문한 적이 없는 곳이라면 깊이 우선 탐색
        if not visited[elem]:
            dfs(elem)


## 변수 입력 부분 ##
n, m = map(int, input().split())
grid = [[] for _ in range(n + 1)]  # 그래프를 인접 그래프로 표현
visited = [False for _ in range(n + 1)]  # 방문 여부를 판단하는 리스트

## 문제 해결 부분 ##
answer = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    # 양방향 그래프 == 무방향 그래프
    grid[v1].append(v2)
    grid[v2].append(v1)

for i in range(1, n + 1):
    # 방문한 적이 없는 곳이라면 방문
    if not visited[i]:
        dfs(i)
        answer += 1

print(f"{answer}")