def solution(s):
    '''
    while "()" in s:
        if "()" in s:
            s = s.replace("()", "")

    return True if s == "" else False
    '''

    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and stack and stack[-1] == "(":
            stack.pop()

        # 이 케이스를 생각 해야함
        elif s[0] == ")":
            return False

    return len(stack) == 0