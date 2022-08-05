def solution(numbers, target):
    answer = 0
    
    visited = [False for i in range(len(numbers))]
    length = len(numbers)
    
    def DFS(depth, count):
        nonlocal answer
        
        if depth == length:
            if count == target:
                answer += 1
            return
        
        temp1 = count + numbers[depth]
        temp2 = count - numbers[depth]
        depth += 1
        DFS(depth, temp1)
        DFS(depth, temp2)
        
    DFS(0, 0)

    return answer