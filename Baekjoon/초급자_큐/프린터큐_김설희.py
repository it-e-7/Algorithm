import sys
from collections import deque

k = int(sys.stdin.readline())
def printer_queue(num_docs, priorities, target_doc):
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # 큐에 (문서 번호, 중요도) 쌍 추가
    count = 0  # 인쇄한 문서 수 초기화

    while queue:
        doc = queue.popleft()  # 큐의 가장 앞에 있는 문서를 가져옴
        if any(doc[1] < q[1] for q in queue):  # 나머지 문서 중 중요도가 더 높은 문서가 있는지 확인
            queue.append(doc)  # 중요도가 높은 문서가 있으면 큐의 맨 뒤로 이동
        else:
            count += 1  # 현재 문서를 인쇄함
            if doc[0] == target_doc:  # 타겟 문서가 인쇄된 경우
                return count  # 인쇄한 문서 수 반환


for _ in range(k):
    n, m = map(int, sys.stdin.readline().split())
    # m : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수

    docs = deque(list(map(int, sys.stdin.readline().split())))

    print(printer_queue(n, docs, m))


