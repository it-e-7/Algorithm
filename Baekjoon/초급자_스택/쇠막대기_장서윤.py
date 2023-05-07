stick = list(map(str, input()))
stack = []
cnt = 0

n = len(stick)
for l in range(len(stick)):
    if stick[l] == "(":
        stack.append(stick[l])

    else:
        if stick[l-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
