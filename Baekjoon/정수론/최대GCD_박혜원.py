# [9417] 최대GCD
<<<<<<< HEAD
=======

>>>>>>> 558179e449e4d970780cdec61a05b66cbeaf8563
"""
range(start, stop, step)
range(gdc(a,b), 0, -1) --> a,b 중 작은 수부터 1까지 역순으로 반복문 실행
"""


def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i    # 역순으로 반복문이 실행되므로 가장 큰 i 반환


n = int(input())
for _ in range(n):
    num_list = list(map(int, input().split()))
    answer = [1]
    for i in range(0, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            answer.append(gcd(num_list[i], num_list[j]))

    print(max(answer))


# import math

# n = int(input())
# for _ in range(n):
#     num_list = list(map(int, input().split()))
#     answer = [1]
#     for i in range(0, len(num_list)-1):
#         for j in range(i+1, len(num_list)):
#             answer.append(math.gcd(num_list[i], num_list[j]))
<<<<<<< HEAD
#     print(max(answer))
=======
#     print(max(answer))
>>>>>>> 558179e449e4d970780cdec61a05b66cbeaf8563
