# [2960] 에라토스테네스의 체
"""
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

K번째 지워진 수를 출력한다.
"""
N, K = map(int, input().split())  # 7, 3
n_list = [False] * (N+1)
count = 0

for i in range(2, N+1):  # 2,3,4,5,6,7
    if n_list[i] == False:
        for j in range(i, N+1, i):  # [순서] 2의배수 지우기 -> 3의배수 지우기 -> ...
            if n_list[j] == False:  # 지운수는 False -> True로 표시
                n_list[j] = True
                count += 1
                if count == K:
                    print(j)  # 2, 4, "6"
