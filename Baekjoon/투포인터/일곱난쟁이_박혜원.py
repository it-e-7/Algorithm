# [2309] 일곱난쟁이

heights = []
for _ in range(9):
    heights.append(int(input()))

# print(heights) [20, 7, 23, 19, 10, 15, 25, 8, 13]


def nanjange(li):
    for i in heights:
        for j in heights:
            if i != j:
                if sum(heights) - (i + j) == 100:
                    heights.remove(i)
                    heights.remove(j)
                    return sorted(heights)


# nanjange(heights)
answer = nanjange(heights)
for i in answer:
    print(i)
