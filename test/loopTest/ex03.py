# 배경: MyBatis로 실행되는DB 쿼리를 모니터링하는 도구입니다.
    # 요구사항
        # - 쿼리 유형(SELECT / INSERT / UPDATE / DELETE)을 입력받아 각각의 실행 횟수를 누적합니다.
        # - 'REPORT' 입력 시 현재까지의 쿼리별 실행 횟수와 총 실행 횟수 출력
        # - 'EXIT' 입력 시 최종 리포트를 출력하고 종료- 그 외 입력은'알 수 없는 쿼리 유형입니다.' 출력
        # - SELECT가 전체의 70% 이상이면 'SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.' 출력


cntSelect = 0
cntInsert = 0
cntUpdate = 0
cntDelete = 0
while True:
    type = input("쿼리 유형 입력: ").upper()
    if type == "SELECT":
        cntSelect += 1
    elif type == "INSERT":
        cntInsert += 1
    elif type == "UPDATE":
        cntUpdate += 1
    elif type == "DELETE":
        cntDelete += 1
    elif type == "REPORT":
        cntTotal = cntSelect + cntInsert + cntUpdate + cntDelete
        print("--- 쿼리 실행 현황 ---")
        print(f"SELECT : {cntSelect}회")
        print(f"INSERT : {cntInsert}회")
        print(f"UPDATE : {cntUpdate}회")
        print(f"DELETE : {cntDelete}회")
        print(f"총 실행 : {cntTotal}회")
        print()
        if cntSelect/cntTotal*100 >= 70:
            print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요")
    elif type == "EXIT":
        print("종료")
        break
    else :
        print("알 수 없는 쿼리 유형입니다.")
