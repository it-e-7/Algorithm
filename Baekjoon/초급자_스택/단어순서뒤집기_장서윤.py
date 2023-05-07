N = int(input())

stack = []

for i in range(N):
    L = input()
    L = L.split(' ')
    w = len(L)

    for word in L:
        stack.append(word)

    print("Case #%d: " %(i+1), end='')

    for _ in range(w):
        print("%s" %(stack.pop()), end=' ')
