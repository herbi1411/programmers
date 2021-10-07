def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        cur = phone_book[i]
        nextval = phone_book[i+1]
        
        if len(cur) <= len(nextval) and cur == nextval[:len(cur)]:
            answer = False
            break
    return answer