from collections import deque

def solution(s):
    answer = True
    q = deque(list(s))

    if q[0] == ")" or q[-1] == "(":
        return False

    open_cnt = 0
    while q:
        checking = q.popleft()
        if checking == "(":
            open_cnt += 1
        elif open_cnt > 0:
            open_cnt -= 1
        else:
            return False

    if open_cnt != 0:
        return False
    return True