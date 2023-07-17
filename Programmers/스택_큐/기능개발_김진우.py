from collections import deque
progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            print(f'progresses, speeds : {progresses, speeds}')
        count = 0
        print(f"***progresses and progresses[0] : {progresses , progresses[0]}")
        while progresses and progresses[0] >= 100:
            # progresses 리스트가 비어있지 않은동안은 계속 반복 + 가장 앞에 있는 기능이 100% 이상일 경우 배포
            progresses.popleft()
            speeds.popleft()
            print("while문")
            print(f'progresses : {progresses} /// speeds : {speeds}')
            count += 1
            print(count)
        if count > 0:
            answer.append(count)

    return answer

solution(progresses,speeds)