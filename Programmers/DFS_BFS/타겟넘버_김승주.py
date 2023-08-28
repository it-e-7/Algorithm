def solution(numbers, target):
    
    n = len(numbers)
    count = 0
    def dfs(i, result):
        
        if(i== n):
            if(result == target):
                nonlocal count
                count+=1
            return 
        else:
            dfs(i+1, result + numbers[i])
            dfs(i+1, result - numbers[i])
    dfs(0,0)

    return count