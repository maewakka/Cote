def solution(clothes):
    answer = 1
    clothes_hash = {}
    
    for cloth in clothes:
        cloth_type = cloth[1]
        cloth_name = cloth[0]
        
        if not cloth_type in clothes_hash:
            clothes_hash[cloth_type] = []
        clothes_hash[cloth_type].append(cloth_name)

    temp = []
    for key in list(clothes_hash.keys()):
        temp.append(len(clothes_hash[key]) + 1)
        
    for i in temp:
        answer *= i
        
    answer -= 1
        
    return answer