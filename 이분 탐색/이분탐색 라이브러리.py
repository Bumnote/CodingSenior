from bisect import bisect_left, bisect_right

num_list = [0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9]

three_l = bisect_left(num_list, 3)
three_r = bisect_right(num_list, 3)
print(f"처음으로 등장하는 3의 위치(bisect_left(num_list, 3)) = {three_l}")
print(f"3 다음으로 등장하는 숫자의 위치(bisect_left(num_list, 3)) = {three_r}")
