import random

dwarf = [int(input()) for _ in range(9)]

while True:
    ran_7 = random.sample(dwarf, 7)  # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
    res = sum(ran_7)
    if res == 100:
        break

seven_dwarfs = sorted(ran_7)

for i in seven_dwarfs:
    print(i)