def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)//2 + 1):
        text = ''
        count = 1
        temp = s[:n]
        
        for i in range(n, len(s)+n, n):
            if temp == s[i:i+n]:
                count += 1
            else:
                if count == 1:
                    text += temp
                else:
                    text += str(count) + temp
                
                temp = s[i:i+n]
                count = 1
                
        if len(text) <= answer:
            answer = len(text)
        

    return answer