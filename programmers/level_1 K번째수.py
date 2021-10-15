def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        slicelist = array[i-1:j]
        slicelist.sort()
        answer.append(slicelist[k-1])
    
    return answer
