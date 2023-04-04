a, b, d = map(int, input().split())

'''
# set이 메모리 사용량이 너무 큼ㅡㅡ

nums = set(range(2, b + 1))
for i in range(2, b + 1):
    if i in nums:
        nums -= set(range(2*i, b+1, i))
'''

nums = [1]*(b+1)
for i in range(2, b + 1):
    if nums[i] == 1:
        j = 2
        while i * j < b + 1:
            nums[i*j] = 0
            j += 1

cnt = 0
for i in range(a, b + 1):
    if nums[i] == 1 and str(d) in str(i):
        cnt += 1

print(cnt)