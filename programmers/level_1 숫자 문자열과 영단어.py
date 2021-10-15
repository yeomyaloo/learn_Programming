def solution(s):
    answer = ''
    a = ['zero', 'one', 'two', 'three','four','five','six','seven','eight','nine']
    for key,values in enumerate(a):
        if values in s:
            s=s.replace(values,str(key))
        answer = s  
    
    return int(answer)
