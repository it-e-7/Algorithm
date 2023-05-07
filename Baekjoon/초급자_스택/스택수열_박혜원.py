# [1874] 스택수열

n = int(input())

stack = []
answer = []
check = True
start_num = 1
for _ in range(n):
    num = int(input())  # 4
    while start_num <= num:
        stack.append(start_num)  # stack = 1,2,3,4
        answer.append("+")  # answer = + + + +
        start_num += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        check = False

if check == False:
    print("NO")
else:
    for i in answer:
        print(i)
