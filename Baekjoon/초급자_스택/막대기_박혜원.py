# [17680] 막대기
import sys
n = int(sys.stdin.readline())
bar_stack = []

for _ in range(n):
    bar_stack.append(int(sys.stdin.readline()))  # [6,9,7,6,4,6]

max_bar_size = bar_stack[-1]
count = 1  # 첫 번째 막대는 항상 보이니까


# for bar_size in bar_stack[::-1]:
#     if bar_size > max_bar_size:
#         max_bar_size = bar_size
#         count += 1

for bar_size in reversed(bar_stack):
    if bar_size > max_bar_size:
        max_bar_size = bar_size
        count += 1

print(count)
