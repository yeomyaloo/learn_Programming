if __name__ =="__main__":
    N, T, C, P = map(int,input().split())
    answer = 0
    result = ((N-1)//T)*P*C
    print(result)