import sys
from math import gcd

a, d = map(int, sys.stdin.readline().split())
q = int(sys.stdin.readline())

for _ in range(q):
    how, l, r = map(int, sys.stdin.readline().split())
    if how == 1:
        print(int((r-l+1)*(a+(l-1)*d + a+(r-1)*d)//2))
    else:
        if l == r:
            print(a+(l-1)*d)
        else:
            print(gcd(a, d))



