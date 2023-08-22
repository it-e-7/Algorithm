def solution(N, number):
    dp = [[] for _ in range(9)]

    for checking in range(1, 9):
        possibles = set()
        raw_Ns = int(str(N) * (checking))
        possibles.add(raw_Ns)

        for i in range(1, checking):

            for num1 in dp[i]:
                for num2 in dp[checking - i]:
                    possibles.add(num1 + num2)
                    possibles.add(num1 - num2)
                    possibles.add(num1 * num2)
                    if num2 != 0:
                        possibles.add(num1 // num2)

        if number in possibles:
            return checking

        dp[checking] = possibles

    return -1

print(solution(5, 12))
print(solution(5, 31168))
print(solution(2, 11))