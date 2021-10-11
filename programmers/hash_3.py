def solution(clothes):
    answer = 0
    cloths = {}
    
    for name,clothtype in clothes:
        if clothtype in cloths:
            cloths[clothtype] += 1
        else:
            cloths[clothtype] = 1
    
    answer = 1
    for key, value in cloths.items():
    #각 아이템의 개수를 한 개씩 뽑아오기.
        answer *= (value + 1)
		#해당 아이템을 착용하지 않을 경우를 고려해서 +1
    return answer - 1
    #모두 입지 않은 경우를 고려해서 -1
