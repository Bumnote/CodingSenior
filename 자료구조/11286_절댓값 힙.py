from sys import stdin
from heapq import heappop, heappush  # 파이썬은 최소 힙 구현
input = stdin.readline

# 변수 선언 부분 #
n = int(input().strip())
num_list = []

# 문제 해결 부분 #
for _ in range(n):
    num = int(input().strip())
    # 숫자가 0이면 절댓값이 가장 작은 값을 출력하고, 제거
    # 절댓값이 같다면 작은 수를 제거
    if num == 0:
        # 숫자가 0인데 배열이 비어있으면 0 출력
        print(heappop(num_list)[1] if num_list else 0)
    # 숫자가 0이 아니면 배열에 삽입
    else:
        heappush(num_list, (abs(num), num))

"""
# 다른 풀이 --> 우선순위 큐를 2개 사용 #
min_heap = [] # 양수 보관 --> 1, 2, 3, 8, 13, 99, 242
max_heap = [] # 음수 보관 --> -1, -4, -10, -1042 
# 양수는 절댓값과 숫자의 크기가 같지만
# 음수는 절댓값이 작을수록 큰 수이다. 

for _ in range(int(input())):
    x = int(input())
    if x:
        if x > 0:
            heappush(min_heap, x)
        else:
            heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(heappop(min_heap))
                else:
                    print(-heappop(max_heap))
            else:
                print(heappop(min_heap))
        else:
            if max_heap:
                print(-heappop(max_heap))
            else:
                print(0)
    
"""