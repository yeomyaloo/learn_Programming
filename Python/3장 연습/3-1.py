#while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key:Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1   
            #검색 실패하면 -1을 반환
        
        if a[i] == key:
            return i
        #검색 성공하면 현재 검사한 배열의 인덱스를 반환
        i += 1

        
if __name__ =='__main__':
    num  = int(input('원소 수를 입력하세요.: '))
    x = [None] *num #입력받은 값만큼 빈리스트 생성

    for i in range(num): #입력받은 num값만큼 반복해서 x[i]값을 입력받아 넣어주기 리스트 채워넣는 개념
        x[i] = int(input(f"x{[i]}: "))

    ky = int(input("검색할 값을 입력하세요.: ")) #검색할 키값을 입력받음

    idx = seq_search(x,ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")
