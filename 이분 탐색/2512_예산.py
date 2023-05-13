from sys import stdin

input = stdin.readline

# 변수 입력 부분 #
n = int(input().strip())  # n: 지방의 수
num_list = list(map(int, input().split()))  # 각 지방마다 요청한 예산
m = int(input().strip())  # m: 총 예산

# 문제 해결 부분 #
# 지방마다 요청한 예산의 합이 총 예산보다 이하인 경우
if sum(num_list) < m:
    print(max(num_list))
# 지방마다 요청한 예산의 합이 총 예산을 초과한 경우 --> 적절한 상한선 설정
else:
    low = 1
    high = max(num_list)
    answer = 0
    # 이진 탐색
    while low <= high:
        mid = (low + high) // 2
        total_num = sum([min(elem, mid) for elem in num_list])
        if total_num <= m:
            low = mid + 1
            answer = max([min(elem, mid) for elem in num_list])
        else:
            high = mid - 1

    print(answer)
