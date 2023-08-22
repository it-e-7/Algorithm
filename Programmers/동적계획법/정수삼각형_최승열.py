def solution(triangle):
    for r in range(len(triangle)-1, 0, -1):
        for c in range(len(triangle[r])-1):
            triangle[r-1][c] += max(triangle[r][c], triangle[r][c+1])
    return triangle[0][0]