from sys import stdin, maxsize

input = stdin.readline


def solve():
    answer = maxsize  # 최솟값을 얻기 위해서 가장 최대인 값으로 설정
    # 각 기준점을 순환한다.
    for y in range(n - 8 + 1):
        for x in range(m - 8 + 1):
            cnt_w, cnt_b = 0, 0  # cnt_w: 시작이 W일 때 바꿔야 할 횟수, cnt_b: 시작이 B일 때 바꿔야 할 횟수
            # 해당 기준점에 대해서 8 * 8 완전 탐색 실행
            for my in range(8):
                for mx in range(8):
                    # 시작이 "W"인 경우 -> 좌푯값이 짝수이면 "W", 홀수이면 "B" 이어야 한다.
                    if (((my + mx) % 2) == 1 and board[y + my][x + mx] != "B") or (
                            ((my + mx) % 2) == 0 and board[y + my][x + mx] != "W"):
                        cnt_w += 1
                    # 시작이 "B"인 경우 -> 좌푯값이 짝수이면 "B", 홀수이면 "W" 이어야 한다.
                    if (((my + mx) % 2) == 1 and board[y + my][x + mx] != "W") or (
                            ((my + mx) % 2) == 0 and board[y + my][x + mx] != "B"):
                        cnt_b += 1

            answer = min(answer, cnt_w, cnt_b)
            # cnt 값이 0인 경우 -> 체스판이 완벽하므로 바로 return
            if answer == 0:
                return 0
    # cnt 값이 0이 나오지 않았다면, 완전탐색 후 가장 적게 바꾼 횟수를 return
    return answer


## 변수 입력 부분 ##
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

## 문제 해결 부분 ##
# 완전 탐색 탐색 -> 각 인덱스마다 8 * 8 탐색을 해서 값을 모두 구한다.
print(solve())