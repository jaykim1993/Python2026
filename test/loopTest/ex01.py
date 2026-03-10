while True:
    user_input = input("상태코드 입력 (종료하려면 '그만' 입력): ")

    if user_input == "그만":
        print("상태확인을 종료합니다.")
        break

    if not user_input.isdigit():
        print("숫자 또는 '그만'을 입력해주세요.")
        continue

    status = int(user_input)
    statusMsg = ""  # 상태 메세지
    cateMsg = "" # 계열 메세지
    # 상태 메세지
    if status == 200:
        statusMsg = "OK - 요청 성공"
    elif status == 201:
        statusMsg = "Created - 리소스 생성 성공"
    elif status == 400:
        statusMsg = "Bad Request - 잘못된 요청"
    elif status == 401:
        statusMsg = "Unauthorized - 인증 필요"
    elif status == 403:
        statusMsg = "Forbidden - 접근 권한 없음"
    elif status == 404:
        statusMsg = "Not Found - 리소스 없음"
    elif status == 500:
        statusMsg = "Internal Server Error - 서버 내부 오류"
    else:
        statusMsg = "Unknown Status Code"
    # 계열 메세지
    if 200 <= status < 300:
        cateMsg = "2xx - 성공"
    elif 400 <= status < 500:
        cateMsg = "4xx - 클라이언트 오류"
    elif 500 <= status < 600:
        cateMsg = "5xx - 서버 오류"
    else:
        cateMsg = "알 수 없는 계열"

    print(f"상태: {status} {statusMsg}")
    print(f"계열: {cateMsg}")
    print("-" * 30)