def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            #p2가 p1으로 시작되면?
            return False
    return True
