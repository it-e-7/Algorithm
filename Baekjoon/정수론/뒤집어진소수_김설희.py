# PyPy3 로 제출 완^o^

num = input()
dic = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
rev_num = ""
check = True
def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in num:
    if i not in dic:
        check = False
        rev_num = '0'
        break
    else:
        rev_num += dic.get(i)

rev_num = rev_num[::-1]

if isprime(int(num)) and isprime(int(rev_num)) and check:
    print("yes")
else:
    print("no")