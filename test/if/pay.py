name = input("이름을 입력하세요: ")
payPerHour = int(input("시급을 입력하세요(원): "))
workHour = int(input("하루 근무 시간을 입력하세요(h): "))
workDays = int(input("근무 일수를 입력하세요(일): "))
startTime = int(input("근무 시작 시간을 입력하세요(0~23): "))

# 주 근무 시간
workHourPerWeek = workHour * workDays
# 야간근무 판별
if (startTime >= 22 and startTime <= 24):
    nightCheck = f"해당있음 (시급 {int(payPerHour*1.5):,}원 적용)"
    nightHour = workHour - (24-startTime)
    
elif (startTime >= 0 and startTime <= 6):
    nightCheck = f"해당있음 (시급 {int(payPerHour*1.5):,}원 적용)"
    nightHour = 6-startTime
else:
    nightCheck = "해당없음"
    nightHour = 0
dayHour = workHour - nightHour
payTotalperDay = int(dayHour*payPerHour + nightHour*payPerHour*1.5)
payTotalperWeek = payTotalperDay*workDays
# 주휴수당 판별
if workHourPerWeek >= 15:
    perWeekcheck = "해당있음"
    perWeekPay = payTotalperDay
else:
    perWeekcheck = "해당없음"
    perWeekPay = 0

tax = int((payTotalperDay + perWeekPay)*3.3/100)
print("="*60)
print(f"{'급여명세서':^55}")
print("="*60)
print(f"{'이름':<12}: {name}")
print(f"{'시급':<12}: {payPerHour:,}원")
print(f"{'근무시간':<10}: {workHourPerWeek:}시간 ({workHour}h x {workDays}일)")
print(f"{'야간근무':<10}: {nightCheck}")
print(f"{'주휴수당':<10}: {perWeekcheck}")
print("="*60)
print(f"{'기본급':<11}: {payTotalperWeek:,}원")
print(f"{'주휴수당':<10}: {perWeekPay:,}원")
print(f"{'세금(3.3%)':<12}: {tax:,}원")
print("-"*60)
print(f"{'실수령액':<10}: {(payTotalperWeek+perWeekPay-tax):,}원")
print("="*60)