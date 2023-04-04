# [23888] 등차수열과 쿼리 (실버 1)
import sys
input = sys.stdin.readline
a, d = map(int, input().split())
q = int(input())

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

cmd_list = []
a_list = []
max_idx = 0
for _ in range(q):
    cmd, s, e = map(int, input().split())
    if max_idx < e:
        max_idx = e
    cmd_list.append([cmd, s, e])

for cmd, s, e in cmd_list:
    if cmd == 1:
        S1 = e*(2*a + d*(e-1))//2
        S2 = (s-1)*(2*a + d*(s-2))//2
        print(S1-S2)
    elif cmd == 2:
        if (s==e):
            print(a+(s-1)*d)
        else:
            print(GCD(a, d))