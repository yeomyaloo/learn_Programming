def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            cnt1 +=1
        if answers[i] == supo2[i]:
            cnt2 +=1
        if answers[i] == supo3[i]:
            cnt3 +=1
            
    if cnt1 > cnt2 and cnt1>cnt3:
        answer.append(1)
    elif cnt2 > cnt1 and cnt2 > cnt3:
        answer.append(2)
    elif cnt3 > cnt1 and cnt3 > cnt2:
        answer.append(3)
    elif cnt1 == cnt2 and cnt1 > cnt3:
        answer.append(1)
        answer.append(2)
    elif cnt3 == cnt2 and cnt3 > cnt1:
        answer.append(2)
        answer.append(3)
    else:
        answer.append(1)
        answer.append(2)
        answer.append(3)
        
    return answer
