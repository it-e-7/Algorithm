n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)

# 절단기 기준을 mid로 잡을 거임
while left <= right:
    mid = (left + right)//2
    cut = 0

    for tree in trees:
        if tree >= mid:
            cut += (tree - mid)

    if cut >= m: # 목표값 이상이면 시작점 옮기고
        left = mid + 1
    else:        # 목표값 이하이면 끝점 옮기기
        right = mid - 1

# 기준 찾은거
print(right)