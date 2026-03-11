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

monthly = {}
for transaction in transactions:
    if transaction[0] not in monthly:
        monthly[transaction[0]] = transaction[1]
    else:
        monthly[transaction[0]] += transaction[1]

total = 0
print("=== 월별 매출 ===")
for month in monthly:
    print(f"{month} : {monthly[month]}원")
    total += monthly[month]

max = 0
maxMonth = ""
for month in monthly:
    if monthly[month] > max:
        max = monthly[month]
        maxMonth = month

min = max
minMonth = ""
for month in monthly:
    if monthly[month] < min:
        min = monthly[month]
        minMonth = month

print(f"최고 매출 월 : {maxMonth} - {max:,}원")
print(f"최소 매출 월 : {minMonth} - {min:,}원")
avr = int(total / len(monthly))
print(f"월 평균 매출 : {avr:,}원")


    

