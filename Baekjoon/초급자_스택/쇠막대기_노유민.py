import sys

input_list=sys.stdin.readline()

stick=0
count=0
for i in range(len(input_list)-1):
    if input_list[i]=='(':
        stick+=1
    else:
        if input_list[i-1]=='(':
            stick-=1
            count+=stick
        else:
            count+=1
            stick-=1
print(count)

