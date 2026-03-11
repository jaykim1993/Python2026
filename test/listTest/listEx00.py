products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]
total = 0

print("=== 재고 현황 ===")
for i in range(len(products)):
    stockCondition = ""
    total += stocks[i]

    if stocks[i] < 10:
        stockCondition = "[재고 부족]"
    # f-string 안에서 바로 조건 판단하기
    # print(f"{products[i]}: {stocks[i]}개 ({'정상' if stocks[i] > 5 else '부족'})")
    
    # print(f"{products[i]}: {stocks[i]}개 {stockCondition}")
    print(products[i] + ": " + str(stocks[i]) + "개 " + stockCondition)
print()
print(f"전체 재고 합계: {total}개")
