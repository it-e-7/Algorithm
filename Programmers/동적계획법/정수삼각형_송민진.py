def solution(triangle):
    for d in range(len(triangle)-1, 0, -1):
        for i in range(1, len(triangle[d])):
            triangle[d-1][i-1] = max(triangle[d-1][i-1] + triangle[d][i-1], triangle[d-1][i-1] + triangle[d][i])
    return triangle[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))