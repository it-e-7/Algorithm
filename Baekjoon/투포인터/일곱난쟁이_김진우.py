'''
li = [int(input()) for _ in range(9)]
# li = [7, 8, 10, 13, 15, 19, 20, 23, 25]
li.sort()

sum_li = sum(li)
to_remove = []
# print(li, sum_li)

for i in range(9):
    for j in range(i+1, 9):
        if sum_li - li[i] - li[j] == 100:
            to_remove.append(li[i])
            to_remove.append(li[j])
            break

for x in to_remove:
    li.remove(x)

for k in li:
    print(k)
'''
'''li = [int(input()) for _ in range(9)]
total = sum(li)

for i in range(9):
    for j in range(i+1, 9):
        if total - li[i] - li[j] == 100:
            del li[j]
            del li[i]
            break

li.sort()
for x in li:
    print(x)

'''
li = [int(input()) for _ in range(9)]
total = sum(li)

for i in range(8):
    for j in range(i+1, 9):
        if total - li[i] - li[j] == 100:
            li.pop(j)
            li.pop(i)
            break
    else:
        continue  # inner loop에서 break 없이 빠져나올 경우 실행
    break  # outer loop에서 break가 실행되면 for문 종료

li.sort()
for x in li:
    print(x)
