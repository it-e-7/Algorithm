n, k = map(int, input().split())
pots = [int(input()) for _ in range(n)]

pots.sort()

'''
테케2
427, 541, 774, 822
11명에게 205씩 나누어주면,
2 2 3 4 -> 11명 완료
'''

left, right = 1, pots[-1]
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for pot in pots:
        mak = pot // mid
        cnt += mak

    if cnt >= k:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)
