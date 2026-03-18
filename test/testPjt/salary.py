# 직원 정보 (리스트 안에 딕셔너리 형태)
# 각 직원은 직원ID, 이름, 부서, 직급, 기본급, 성과급, 초과근무수당, 식대, 교통비 정보를 가진다.
employees = [
{'id':'E001','name':'김철수','dept':'개발팀','grade':'대리','base':3200000,'bonus':500000,'overtime':200000,'meal':100000,'transport':80000},
{'id':'E002','name':'이영희','dept':'개발팀','grade':'과장','base':4100000,'bonus':800000,'overtime':0,'meal':100000,'transport':80000},   
{'id':'E003','name':'박민준','dept':'영업팀','grade':'사원','base':2800000,'bonus':300000,'overtime':150000,'meal':100000,'transport':80000},
{'id':'E004','name':'최수진','dept':'영업팀','grade':'대리','base':3500000,'bonus':600000,'overtime':100000,'meal':100000,'transport':80000},
{'id':'E005','name':'정다은','dept':'인사팀','grade':'과장','base':3900000,'bonus':700000,'overtime':50000,'meal':100000,'transport':80000},
{'id':'E006','name':'한지호','dept':'인사팀','grade':'사원','base':2600000,'bonus':200000,'overtime':80000,'meal':100000,'transport':80000}
]
  
# 공제율 (고정값)
TAX_RATE   = 0.033   # 소득세 3.3%
INSURANCE_RATE  = 0.045   # 4대보험 4.5%

salary_emp = dict() # 급여 관련 정보를 담고 있는 개인 딕셔너리 calsulate_salary 들어갔다 나와서 전체 급여 리스트로 후가공


# 1. 전체 직원 목록 조회 함수
def show_employees():
    print("--------------------------------------------")
    print("직원ID\t 이름\t 부서\t 직급\t 기본급")
    print("--------------------------------------------")
    for emp in employees:
        print(f"{emp['id']}\t {emp['name']}\t {emp['dept']}\t {emp['grade']}\t {emp['base']:,}원")
    return

# 급여 계산 함수
def calculate_salary(id):
    for emp in employees:
        if id == emp['id']:
            salary_emp = emp
            salary_emp['total'] = emp['base'] + emp['bonus'] + emp['overtime'] + emp['meal'] + emp['transport']
            salary_emp['tax'] = int(emp['base']*33/1000)
            salary_emp['insurance'] = int(emp['base']*45/1000)
            salary_emp['deduction'] = salary_emp['tax'] + salary_emp['insurance']
            salary_emp['salary'] = salary_emp['total'] - salary_emp['deduction']
    return salary_emp

# 개인 급여 명세서 출력
def show_payslip(result) :
    print("\n---------------------------------------")
    print("\n[직원 정보]")
    print(f" - {'직원명':<8} : {result['name']}\n - {'부서':<9} : {result['dept']}\n - {'직급':<9} : {result['grade']}\n")
    print("[지급 내역]")
    print(f" - {'기본급':<8} : {result['base']:>12,} 원\n - {'성과급':<8} : {result['bonus']:>12,} 원\n - {'초과근무수당':<6} : {result['overtime']:>12,} 원\n - {'식대':<9} : {result['meal']:>12,} 원\n - {'교통비':<8} : {result['transport']:>12,} 원\n - {'총 지급액':<7} : {result['total']:>12,} 원\n")
    print("[공제 내역]")
    print(f" - {'소득세(3.3%)':<6} : {result['tax']:>12,} 원\n - {'4대보험(4.5%)':<5} : {result['insurance']:>12,} 원\n - {'총 공제액':<7} : {result['deduction']:>12,} 원\n")
    print(f"[실수령액]\n - {result['salary']:,} 원")
    return

# 전체 급여 현황
def show_all_salary() :
    print("-"*66)
    print("이름\t 기본급\t\t 총지급액\t 총공제액\t 실수령액")
    print("-"*66)
    for emp in employees:
        result = calculate_salary(emp['id'])
        print(f"{result['name']}\t {result['base']:,}\t {result['total']:,}\t {result['deduction']:,}\t {result['salary']:,}")
    return

# 부서별 급여 통계
def show_dept_stats():
    salary_dept = {}  # 부서별 급여 통계 딕셔너리 

    for emp in employees:
        result = calculate_salary(emp['id'])
        dept = result['dept']
        
        if dept not in salary_dept:
            salary_dept[dept] = {
                'dept': dept, 
                'memberCnt': 1, 
                'totalBase': result['base'], 
                'totalSal': result['salary']
            }
        else:
            salary_dept[dept]['memberCnt'] += 1
            salary_dept[dept]['totalBase'] += result['base']
            salary_dept[dept]['totalSal'] += result['salary']

    print("-"*46)
    print("부서\t 인원\t 기본급합계\t 평균 실수령액")
    print("-"*46)
    for dept in salary_dept:
        avgSal = int(salary_dept[dept]['totalSal'] / salary_dept[dept]['memberCnt'])
        print(f"{salary_dept[dept]['dept']}\t {salary_dept[dept]['memberCnt']}명\t {salary_dept[dept]['totalBase']:,}\t {avgSal:,}")
    return 

# 급여 순위 조회
def show_salary_rank() :
    salarys = []
    rankList = []
    for emp in employees:
        result = calculate_salary(emp['id'])
        salarys.append(result['salary'])

    salarys.sort(reverse=True) # 샐러리 정렬
    # print(salarys)

    for emp in employees:
            result = calculate_salary(emp['id'])
            for i in range(len(salarys)):
                if result['salary'] == salarys[i]:
                    rankList.append(f"{i+1}\t {result['name']}\t {result['dept']}\t {result['grade']}\t {result['salary']:,} 원")
                    break 
    rankList.sort() # 문자열의 시작이 1,2,3이므로 소팅 시 급여순으로 
    # print(rankList)

    print("순위\t 이름\t 부서\t 직급\t 급여")
    print("-" * 45)
    for rank_info in rankList:
        print(rank_info)
    return 


# 뒤로가기 함수
def backMenu():
    back = input("\n뒤로가기 - ENTER")



# list.sorted('기본급')


# 시스템 구동 구문
while True:
    print("\n=== 직원 급여 관리 시스템 ===\n")
    print("  1. 전체 직원 목록 조회")
    print("  2. 급여 명세서 출력 (개인)")
    print("  3. 전체 급여 현황")
    print("  4. 부서별 급여 통계")
    print("  5. 급여 순위 조회")
    print("  0. 종료\n")
    optionA = input("메뉴를 선택하세요: ")
    if optionA == "1":
        print("\n• 전체 직원 목록 조회")
        show_employees()
        backMenu()
    elif optionA == "2":
        print("\n• 급여 명세서 (개인)\n")
        while True:
            inputID = input("직원ID를 입력하세요: ").upper()
            result = None
            for emp in employees:
                if emp['id'] == inputID:
                    result = inputID
            if result == None:
                print("\n！존재하지 않는 ID입니다！\n")
            else: break
        emp = calculate_salary(result)
        show_payslip(emp)
        backMenu()
    elif optionA == "3":
        print("\n• 전체 급여 현황")
        show_all_salary()
        backMenu()
    elif optionA == "4":
        print("\n• 부서별 급여 통계")
        show_dept_stats()
        backMenu()
    elif optionA == "5":
        print("\n• 급여 순위 조회")
        show_salary_rank()
        backMenu()
    elif optionA == "0":
        print("\n• 종료")
        break
    else :
        print("\n  0 - 5 사이 숫자를 입력하세요")