n = int(input())
k = int(input())

'''
k = 7일때 k보다 작거나 같은 숫자의 개수
1 2 3   3개
2 4 6   3개
3 6 9   1개

k = 7일 때 답은 6
'''

start, end = 1, n*n
# 인덱스 1부터~
while start <= end:
    mid = (start + end)//2
    # (1 + n*n)//2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid // i, n)
        # 한 행에서 3개 or (5//행넘버)개
        # 규칙 찾기
    if cnt >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)
