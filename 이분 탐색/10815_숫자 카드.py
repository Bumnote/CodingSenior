from sys import stdin

input = stdin.readline

# 변수 입력 부분 #
n = int(input().strip())  # 상근이가 가지고 있는 숫자의 개수
n_list = list(map(int, input().split()))  # 상근이가 가지고 있는 숫자 리스트
m = int(input().strip())
m_list = list(map(int, input().split()))

# 문제 해결 부분 #
n_list.sort()  # 이진 탐색을 위해 오름차순 정렬
for elem in m_list:
    low = 0
    high = n - 1
    flag = False
    while low <= high:
        mid = (low + high) // 2
        if n_list[mid] == elem:
            flag = True
            break
        elif n_list[mid] < elem:
            low = mid + 1
        else:
            high = mid - 1

    print(1 if flag else 0, end=" ")
