orderCnt = 0
totalPrice = 0
totalDiscount = 0
totalPay = 0

# while 시작
while True:
    inputGrade = input("회원등급 (END 종료): ").lower()
    if inputGrade == "end":
        break
    elif inputGrade  not in ["bronze", "silver", "gold", "vip"]:
        print("등록되지 않은 등급입니다.")
    else :
        inputPrice = int(input("구매금액: "))
        
        # 등급별 할인율 조건
        if inputGrade == "bronze":
            discount = 0
        if inputGrade == "silver":
            discount = int(inputPrice * 5 / 100)
        if inputGrade == "gold":
            discount = int(inputPrice * 10 / 100) + 5000
        if inputGrade == "vip":
            discount = int(inputPrice * 20 / 100) + 10000

        # 할인금액이 더 클 경우 결제금액 0원
        if inputPrice > discount:
            payPrice = inputPrice-discount
        else:
            payPrice = 0
        
        # 등급별 출력
        print(f"할인금액: {discount:,}원  ->  결제금액: {payPrice:,}원")

        # 전체 누적 ++
        orderCnt += 1
        totalPrice += inputPrice
        totalDiscount += discount
        totalPay += payPrice

# 전체 주문 요약 출력
print("--- 전체 주문 요약 ---")
print(f"주문 건수: {orderCnt}")
print(f"총 구매금액: {totalPrice:,}원  |  총 할인: {totalDiscount:,}원  |  총 결제: {totalPay:,}원")
