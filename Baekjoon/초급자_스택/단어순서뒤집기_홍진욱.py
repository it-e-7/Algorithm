def reverse_words(case_num, words):
    reversed_words = words.split()[::-1]
    result = " ".join(reversed_words)
    print("Case #{}: {}".format(case_num, result))

n = int(input())
for case in range(1, n+1):
    words = input()
    reverse_words(case, words)
