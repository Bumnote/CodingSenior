from sys import stdin
from collections import deque

input = stdin.readline


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


# 최단 거리를 구할 때는 주로 BFS 탐색 활용
def bfs(y, x, cnt):
    deq = deque([])
    deq.append((y, x, cnt))  # 최소의 칸 수를 구해야 하므로 BFS 탐색을 위한 덱 선언
    visited[y][x] = False  # 방문 처리
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

    while deq:
        cur_y, cur_x, cur_cnt = deq.popleft()
        for dy, dx in zip(dys, dxs):
            new_y, new_x = cur_y + dy, cur_x + dx
            # 범위를 넘지 않고, 방문한 적이 없고, 이동 가능한(!= 0) 곳이라면 -> 덱에 추가
            if in_range(new_y, new_x) and visited[new_y][new_x] and grid[new_y][new_x] != 0:
                visited[new_y][new_x] = False  # 방문 처리
                grid[new_y][new_x] = cur_cnt + 1
                deq.append((new_y, new_x, cur_cnt + 1))


## 변수 입력 부분 ##
n, m = map(int, input().split())  # n x m 행렬
grid = [list(map(int, input().strip())) for _ in range(n)]  # 1: 이동 가능, 0: 이동 불가능
visited = [[True] * m for _ in range(n)]  # 방문 처리용 리스트

## 문제 해결 부분 ##
bfs(0, 0, 1)
print(grid[n - 1][m - 1])
