import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    s = input().strip()
    stack = []

    for c in s:
        if stack and stack[-1] == c:  # 스택의 맨 위에 있는 문자와 현재 문자가 같은 경우
            stack.pop()  # 스택에서 문자를 제거
        else:
            stack.append(c)  # 스택에 문자를 추가

    if not stack:  # 스택이 비어있는 경우(=좋은 단어인 경우)
        cnt += 1
print(cnt)
