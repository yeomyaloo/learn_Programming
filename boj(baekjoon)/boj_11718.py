while True:
    try:
        print(input())

    except EOFError: #데이터가 없어서 더이상 값을 읽을 수 없을 때 발생하는 
        break
