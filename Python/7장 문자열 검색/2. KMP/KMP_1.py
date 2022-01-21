# KMP법으로 문자열 검색하기

def kmp(txt, pat):

    pt = 1 # 텍스트를 따라가는 커서
    pp = 0 # 패턴을 따라가는 커서

    skip = [0] *( len(pat) + 1) # 건너뛰기 표

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] == pp
        else:
            pp = skip[pp]

        #문자열 검색하기
        pt = pp = 0
        while pt != len(txt) and pp != len(pat):
            if txt[pt] == pat[pp]:
                pt += 1
                pp += 1
            elif pp == 0:
                pt += 1
            else:
                pp = skip[pp]
    return pt - pp if pp == len(pat) else -1

s1 = input("텍스트를 입력하세요.: ")
s2 = input("패턴을 입력하세요.")

idx = kmp(s1,s2)

if idx == -1:
    print("텍스트 안에 패턴이 존재하지 않습니다.")
else:
    print(f"{(idx+1)}번째 문자가 일치합니다.")
