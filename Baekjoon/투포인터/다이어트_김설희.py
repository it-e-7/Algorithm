'''
15 = '현재'^2 - '기억'^2
현재로 가능한 것들, 자연수 아니면 제외, 없으면 -1, 오름차순

현재가 15**0.5보다는 커야함
round(n**0.5)
'''

G = int(input())

start, end = 1, round(G**0.5)
result = []

while True:
    # G = '현재'^2 - '기억'^2
    weight = end ** 2 - start ** 2
    if end - start == 1 and weight > G:
        break

    if weight > G:
        start += 1
    elif weight < G:
        end += 1
    else:
        result.append(end)
        end += 1

if result:
    for i in result:
        print(i)
else:
    print(-1)