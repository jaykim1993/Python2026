tokenNumber = int(input("토큰 수를 입력하세요: "))

waringCnt = 0
goodCnt = 0
for i in range(1, tokenNumber+1):
    inputTime = int(input(f"토큰 {i} 잔여시간(분): "))
    if inputTime <= 0:
        print("[만료] 즉시 재발급 필요")
        waringCnt += 1
    if 1 <= inputTime <= 10:
        print("[위험] 곧 만료됩니다. 갱신 권장")
        waringCnt += 1
    if 11 <= inputTime <= 30 :
        print("[주의] 만료가 가까워지고 있습니다.")
        waringCnt += 1
    if inputTime >= 31:
        print("[정상] 유효한 토큰")
        goodCnt += 1
print("-- 요약 --")
print(f"정상 토큰: {goodCnt}개 / 경고 토큰: {waringCnt}개")