
n = int(input())
numbers = list(map(int,input().split()))

x = int(input())

numbers.sort()

start = 0
end = n-1

count = 0
while start < end :
    if numbers[start] + numbers[end] == x:
        count+=1
    
    if numbers[start] + numbers[end] < x :
        start +=1
    else :
        end -=1

print(count)