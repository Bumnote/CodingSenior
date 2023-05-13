from sys import stdin
input = stdin.readline

def find_vps():
    global items, stack
    for item in items:
        # 열린 괄호라면 stack에 push
        if item == "(":
            stack.append(item)
        # 닫힌 괄호라면
        else:
            # stack에 원소가 있으면서 stack의 top이 열린 괄호라면 pop
            if stack:
                stack.pop()
            # stack의 top이 닫힌 괄호라면 no -> return
            else:
                return False
    if not stack:
        return True
    else:
        return False


n = int(input().strip())
for _ in range(n):
    items = list(input().strip())
    stack = []
    # 가장 첫 원소가 닫힌 괄호라면 -> NO
    if items[0] == ")":
        print("NO")
        continue

    if find_vps():
        print("YES")
    else:
        print("NO")

