checkList = [
    "Db 마이그레이션 완료 여부", 
    "application-prod.properties 설정 확인", 
    "JWT Secret Key 변경 여부", 
    "CORS 허용 도메인 설정 완료", 
    "API 엔드포인트 테스트 통과"
    ]

notDone = 0
notDoneList = []

while True:
    for i in range(len(checkList)):
        check = input(f"[{i+1}/{len(checkList)}] {checkList[i]} (Y/N): ").lower()
        if check == "y":
            print("→ 완료")
        elif check == "n":
            print("→ 미완료")
            notDone += 1
            notDoneList.append(f"   · [{i+1}] {checkList[i]}")
    if notDone == 0:
        print("배포 승인! 배포를 진행하세요")
        break
    else :
        print(f"배포 보류! {notDone}개 항목을 해결 후 재시도하세요.")
        for i in range(len(notDoneList)):
            print(notDoneList[i])
        break