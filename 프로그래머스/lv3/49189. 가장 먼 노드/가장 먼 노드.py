from collections import deque

def solution(n, edge):
    answer = 0
    
    nodes = {}
    result = [0 for i in range(n+1)]
    
    for i in range(1, n+1):
        nodes[i] = []
        
    for node in edge:
        a = node[0]
        b = node[1]
        
        nodes[a].append(b)
        nodes[b].append(a)
        
    for i in range(1, n+1):
        nodes[i] = sorted(nodes[i])
    

    visited = [False for i in range(n)]
    visit_queue = deque()

    visit_queue.appendleft(1)

    while visit_queue:
        this_node = visit_queue.pop()
        visited[this_node-1] = True
        child = nodes[this_node]

        for i in range(len(child)):
            if not visited[child[i]-1] and not child[i] in visit_queue:
                result[child[i]] = result[this_node] + 1
                visit_queue.appendleft(child[i])
                    
    answer = result.count(max(result))
    
    
    return answer