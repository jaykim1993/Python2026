transactions = [
['2024-01', 3200000],
['2024-01', 1500000],
['2024-02', 2800000],
['2024-02', 900000],
['2024-03', 4100000],
['2024-03', 2200000],
['2024-04', 1800000],
['2024-04', 3300000],
['2024-05', 5000000],
['2024-06', 2100000]
]

# 리스트 언팩킹 후 월별 딕셔너리 패킹
monthly = {}

# for transaction in transactions:
# transaction이라는 변수 하나에 리스트 통째를 담음 
# -> 그래서 transaction[0], transaction[1]처럼 인덱스로 접근해야 함.
#     if transaction[0] not in monthly:
#         monthly[transaction[0]] = transaction[1]
#     else:
#         monthly[transaction[0]] += transaction[1]

# month, amount라는 변수 두 개에 리스트 내부 값을 나눠 담음 
# -> 인덱스 없이 이름으로 바로 사용 가능해서 가독성이 훨씬 좋음.
# for문 뒤에 쉼표(,)로 변수를 여러 개 쓰면, 
# 파이썬이 리스트 안의 데이터를 순서대로 넣어줌
for month, amount in transactions:
    if month not in monthly:
        monthly[month] = amount
    else:
        monthly[month] += amount

# 월별 매출 출력, 총 매출 합
total = 0
print("=== 월별 매출 ===")
for month in monthly:
    print(f"{month} : {monthly[month]:,}원")
    total += monthly[month]
avg = int(total / len(monthly))

# 최대 매출 구하기
max = 0
# maxMonth = ""
for month in monthly:
    if monthly[month] > max:
        max = monthly[month]
        maxMonth = month

# 최저 매출 구하기 <- 최대 매출을 최초 비교값으로 선정
min = max
# minMonth = ""
for month in monthly:
    if monthly[month] < min:
        min = monthly[month]
        minMonth = month

# 매출 출력
print(f"최고 매출 월 : {maxMonth} ({max:,}원)")
print(f"최저 매출 월 : {minMonth} ({min:,}원)")
print(f"월 평균 매출 : {avg:,}원")


    

