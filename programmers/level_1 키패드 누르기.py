def solution(numbers, hand):
    answer = ""
    #거리 계산을 위한 좌표 준비 
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    ls = dic['*']
    rs = dic['#']
    
    for i in numbers:
        now = dic[i] #현재 위치
        if i in [1,4,7]:
            answer += "L"
            ls = now
        elif i in [3,6,9]:
            answer += "R"
            rs = now
        else:
            ld = 0
            rd = 0
            for a,b,c in zip(ls,rs,now):
                ld += abs(a-c)
                rd += abs(b-c)
            if ld < rd:
                answer += "L"
                ls = now
            elif ld > rd:
                answer += "R"
                rs = now
            else:
                if hand == "right":
                    answer += "R"
                    rs = now
                else:
                    answer += "L"
                    ls = now
    return answer
