import sys

string = sys.stdin.readline().strip()
stack=[]
results=0

num_stick = 0

for i, s in enumerate(string):
    if s == '(':
        stack.append(s)
        num_stick += 1
    else:
        stack.pop()
        if string[i-1] == '(':
            num_stick -= 1
            results += len(stack)
        else:
            num_stick -= 1
            results += 1

print(results)
