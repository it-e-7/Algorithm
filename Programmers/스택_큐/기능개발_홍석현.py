def solution(progresses, speeds):
    answer = []

    start = 0
    while True:
        if start >= len(progresses):
            break
        for i in range(start, len(progresses)):
            progresses[i] += speeds[i]
        if progresses[start] >= 100:
            success = 1
            for i in range(start + 1, len(progresses)):
                if progresses[i] >= 100:
                    success += 1
                else:
                    break
            answer.append(success)
            start += success

    return answer