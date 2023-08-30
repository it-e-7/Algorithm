answer = 0


def dfs(arr, tmp, length, target):
    global answer

    if tmp == target and len(arr) == length:
        answer += 1
        return

    if len(arr) == length:
        return

    # 값을 빼는 경우, 더하는 경우 분기
    dfs(arr, tmp + arr[length], length + 1, target)
    dfs(arr, tmp - arr[length], length + 1, target)


def solution(numbers, target):
    dfs(numbers, 0, 0, target)

    return answer
