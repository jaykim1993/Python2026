calNumber = int(input("측정 횟수를 입력하세요: "))


avrRes = 0
critialNum = 0
for i in range(1,calNumber+1):
    resTime = int(input(f"응답시간 {i} (ms): "))

    # 응답시간 메세지 출력 조건
    if resTime <= 100:
        print("FAST") 
    elif 100 < resTime <= 300:
        print("NORMAL")
    elif 300 < resTime <= 1000:
        print("SLOW")
    elif 1000 < resTime:
        print("CRITICAL")
        critialNum += 1
    # 초기 최소, 최대 지정
    if i == 1:
        minRes = resTime
        maxRes = resTime
    # 최소, 최대 비교
    else:
        if minRes >= resTime:
            minRes = resTime
        if maxRes <= resTime:
            maxRes = resTime
    avrRes += resTime
# 평균 구하기
avrRes = avrRes/calNumber

print(f"평균 응답시간: {avrRes:.1f}ms")
print(f"최대: {maxRes}ms  |  최소: {minRes}ms")
# CRITICAL 경고 조건
if critialNum/calNumber*100 >= 10:
    print("SLA 위반! 서버 점검이 필요합니다.")