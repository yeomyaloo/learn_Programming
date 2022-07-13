def solution(s):
    a = []
    b = []
    for i in range(len(s)):
        if s[i][0] > s[i][1]:
            a.append(s[i][0])
            b.append(s[i][1])
        else:
            a.append(s[i][1])
            b.append(s[i][0])
                       
    
    return max(a) * max(b)
