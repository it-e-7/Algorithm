n, m = map(int, input().split())

# 팩토리얼의 배수 개수
def cnt(N, M):
    count = 0
    while N > 0:
        N //= M
        count += N
    return count


cnt5 = cnt(n, 5) - cnt(m, 5) - cnt(n - m, 5)
cnt2 = cnt(n, 2) - cnt(m, 2) - cnt(n - m, 2)

print(min(cnt5, cnt2))