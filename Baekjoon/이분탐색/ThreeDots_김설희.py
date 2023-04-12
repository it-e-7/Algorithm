# PyPy3로 제출!

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    cnt = 0

    for i in range(n-1): #왼
        for j in range(i+1, n): #오
            if (nums[i]+nums[j]) % 2 == 0 and (nums[i]+nums[j])//2 in nums[i:j+1]:
                cnt += 1
    print(cnt)
