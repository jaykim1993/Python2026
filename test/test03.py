# 이스케이프문자, 서식문자 이용 영수증 출력
# 파이썬은 변수를 선언할 때 변수선언 명령문이 존재하지 않는다.

# 데이터 준비
order_no = "107818855"
address = "서울시 종로구 종로3가"
name = "김사장"
phone = "070-1234-5678"

# 품목 데이터
item1, p1, q1 = "블루투스 이어폰", 85000, 1
item2, p2, q2 = "USB3.0 8G", 8000, 1

amt1, amt2 = p1*q1, p2*q2
total = amt1 + amt2



# 출력 시작
# 서식문자는 f-string(현재 표준으로 사용)
print(f"{'파이썬 쇼핑몰':^55}") # 55 길이에서 ^(가운데정렬)
print(f"번호 : {order_no}")
print(f"주소 : {address}")
print(f"성명 : {name}")
print(f"전화 : {phone}")
print("-" * 60)

# 헤더(품명 왼쪽, 나머지 오른쪽 정렬)
# <20: 20칸 왼쪽 / >10: 10칸 오른쪽
print(f"{'품명':<20} {'단가':>10} {'수량':>7} {'금액':>10}")
print("-" * 60)

# 천 단위마다 콤마, 출력법 : >10뒤에 ,
print(f"{item1:<18} {p1:>10,} {q1:>7} {amt1:>14,}")
print(f"{item2:<25} {p2:>10,} {q2:>7} {amt2:>14,}")

# 하단 결제 정보
print(f"{'소 계':<46} {total:>10,}")
print("-" * 60)

while True:
    try:
        received = int(input("받은 금액: "))
        change = received - total
        if received >= total:
            print(f"{'받은금액':<44} {received:>10,}")
            print(f"{'청구금액':<44} {-total:>10,}")
            print(f"{'거스름돈':<44} {change:>10,}")
            print("-" * 60)
            print(f"{'이용해주셔서 감사합니다!':^55}")
            break
        else:
            print(f"금액이 {total - received:,}원 부족합니다. 다시 확인해주세요.")
    except ValueError:
            print("숫자만 입력 가능합니다. 다시 시도해주세요.")