def solution(s):
    answer = True

    stack = list()

    for b in s:
        if b == "(":
            stack.append(b)

        else:
            if not stack:
                return False

            else:
                stack.pop()

    if not stack:
        return True

    else:
        return False
