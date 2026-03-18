books = [
    ("파이썬 기초", 15000), 
    ("자바의 정석", 25000), 
    ("React 입문", 18000)
    ]
total = 0

def total_price(books):
    global total
    print("=== 도서 목록 ===")
    for name, price in books:
        total += price
        print(f"도서명: {name}, 가격: {price:,}원")
    print(f"전체 도서 합계 : {total:,}원")
    return

result = total_price(books)

