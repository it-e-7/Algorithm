def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if not stack or stack[-1] == ')':
                return False
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False

# def solution(s):
#     answer = True
#     stack = []
#     for i in s:
#         if not stack:
#             if i == ')':
#                 return False
#             elif i == '(':
#                 stack.append(i)
#         elif i == '(':
#             stack.append(i)
#         elif i == ')':
#             stack.pop()

#     if not stack:
#         return True
#     else:
#         return False