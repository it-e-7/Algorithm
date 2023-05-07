# [10799] 쇠막대기

a = list(input())  # ()(((()())(())()))(())
stack = []
answer = 0
for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])
    else:
        if a[i-1] == "(":   # ()
            stack.pop()
            answer += len(stack)
        else:  # ))
            stack.pop()
            answer += 1
print(answer)
