month = int(input("방문월을 입력하세요(1~12)"))
adult = int(input("성인 인원수 : "))
teen = int(input("청소년 인원수 : "))
kid = int(input("어린이 인원수 : "))
elder = int(input("경로 인원수 : "))



adultPay = 55000 * adult
teenPay = 40000 * teen
kidPay = 28000 * kid
elderPay = 15000 * elder
totalNum = adult + teen + kid + elder
totalPay = adultPay + teenPay + kidPay + elderPay
discountTotal = 0
msg = ""
msgKid = ""
if month == 7 or month == 8:
    monthCheck = "(성수기)"
    msg = "성수기 할인 미적용"
else :
    monthCheck = "(비수기)"
    if totalNum >= 5 and kid < 3:
        discountTotal = totalPay/10
        msg = "(10%)"
    elif totalNum >= 5 and kid >= 3:
        kidPay = 0
        msgKid = "(무료!)"
        msg = "(10%)"
        totalPay = int(adultPay + teenPay + kidPay + elderPay)
        discountTotal = int(totalPay/10)



print("="*28)
print(f"{'놀이공원 입장권 계산서'}")
print("="*28)
print(f"{'방문월':<10}: {month}월 {monthCheck}")
print("="*28)
print(f"{'성인':<6}{adult}명 : {adultPay:>10,} 원")
print(f"{'청소년':<5}{teen}명 : {teenPay:>10,} 원")
print(f"{'어린이':<5}{kid}명 : {kidPay:>10,} 원 {msgKid}")
print(f"{'경로':<6}{elder}명 : {elderPay:>10,} 원")
print("="*28)
print(f"{'소계':<10}: {totalPay:>10,} 원")
print(f"{'단체할인':<8}: {-discountTotal:>10,} 원 {msg}")
print("-"*28)
print(f"{'최종금액':<8}: {totalPay-discountTotal:>10,} 원")
print("="*28)
print(f"{'총 인원':<9}: {totalNum:>10,} 명")