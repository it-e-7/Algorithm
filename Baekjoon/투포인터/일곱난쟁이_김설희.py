nan = sorted([int(input()) for _ in range(9)])

for i in range(len(nan)):
    for j in range(i, len(nan)):
        if nan[i] + nan[j] == sum(nan)-100:
            # j부터 먼저 지워야 됨 안 그러면 인덱스 변형옴
            nan.remove(nan[j])
            nan.remove(nan[i])
            break

for i in nan:
    print(i)