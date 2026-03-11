# Dictionary == Object
# Key : value 가 하나의 세트
# 출력 시 dict["key"] => 해당 key의 value가 출력됨

phone_book = {}
phone_book["홍길동"] = "010-1111-1111"
phone_book["강감찬"] = "010-2222-2222"
phone_book["이순신"] = "010-3333-3333"

# print(phone_book) 
# {'홍길동': '010-1111-1111', '강감찬': '010-2222-2222', '이순신': '010-3333-3333'}
# print(phone_book["이순신"])
# 010-3333-3333
# print(phone_book.keys())
# dict_keys(['홍길동', '강감찬', '이순신'])
# print(phone_book.values())
# dict_values(['010-1111-1111', '010-2222-2222', '010-3333-3333'])

# 문제) phone_book 홍길동 010-1111-111
for name in sorted(phone_book.keys()):
    print(name, phone_book[name])