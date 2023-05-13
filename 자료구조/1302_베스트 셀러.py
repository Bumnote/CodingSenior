from sys import stdin

input = stdin.readline

# 변수 선언 부분 #
n = int(input().strip())

# 문제 해결 부분 #
books = {}

for _ in range(n):
    book_name = input().strip()
    if book_name not in books:
        books[book_name] = 0
    books[book_name] += 1

new_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(new_books[0][0])
