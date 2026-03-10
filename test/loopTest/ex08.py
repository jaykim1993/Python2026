# 파일명: ex08.py

# 1. 초기 데이터 설정
days = ['월', '화', '수', '목', '금', '토', '일']
sales_list = []
target_count = 0

# 2. 목표 매출 및 요일별 매출 입력
target_sales = int(input("목표 일 매출액: "))

print("-" * 30)

for day in days:
    sales = int(input(f"{day}요일 매출: "))
    sales_list.append(sales)
    
    # 매출 등급 판정
    if sales >= target_sales:
        result = "목표 달성"
        target_count += 1
    elif sales >= target_sales * 0.7:
        result = "분발 필요"
    else:
        result = "목표 미달"
        
    print(f"{day}요일 매출: {sales:,}원  →  {result}")

# 3. 데이터 분석
total_sales = sum(sales_list)
avg_sales = total_sales / len(sales_list)

# 최고/최저 매출 계산
max_sales = max(sales_list)
min_sales = min(sales_list)

# 해당 금액의 요일 찾기 (index 활용)
max_day = days[sales_list.index(max_sales)]
min_day = days[sales_list.index(min_sales)]

# 4. 분석 결과 출력
print("-" * 30)
print(f"총 매출: {total_sales:,}원 | 일평균: {avg_sales:,.0f}원")
print(f"최고 매출: {max_day}요일 {max_sales:,}원 | 최저 매출: {min_day}요일 {min_sales:,}원")
print(f"목표 달성: {target_count}일")