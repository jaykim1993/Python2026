# input받기
spot1 = input("출발지 : ")
spot2 = input("목적지 : ")
distance = float(input("이동거리 : "))
time = int(input("탑승시간 : "))
childYesNo = input("어린이 동반유무(y/n) : ")


# 어린이 if문
basicPrice = 0
if childYesNo == "y":
    basicPrice = 0
elif childYesNo == "n":
    basicPrice = 4800
else:
    basicPrice = 4800
distancePrice = 0
# 거리 요금 if문
if distance > 2:
    distancePrice = int(((distance-2)*1000/100) * 100)
# 심야 요금 if문
nightPrice = 0
if (time >= 22 and time <=24) or (time > 0 and time < 4): 
    nightPrice = int((basicPrice + distancePrice)/5)

# 출력문
print("="*60)
print(f"{'택시 요금 안내':^55}")
print("="*60)
print(f"{'출발지   : ':<7} {spot1}")
print(f"{'목적지   : ':<7} {spot2}")
print(f"{'이동거리 : ':<7} {distance} km")
print(f"{'탑승시간 : ':<7} {time}시")
print("="*60)
print(f"{'기본요금 : ':<7} {basicPrice:,}원")
print(f"{'거리요금 : ':<7} {distancePrice:,}원")
print(f"{'심야할증 : ':<7} {nightPrice:,}원  (20%적용)")
print("-"*60)
print(f"{'최종요금 : ':<7} {basicPrice+distancePrice+nightPrice:,}원")