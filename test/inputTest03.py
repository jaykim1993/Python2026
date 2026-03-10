name = input("이름을 입력하세요: ")
height = int(input("키를 입력하세요(cm): "))
weight = int(input("몸무게를 입력하세요(kg): "))
avr_weight = (height-100) * 0.9
borca_katsura = (weight-avr_weight) / avr_weight*100
print("-" * 30)
print(f"{name}님의 비만도는 {borca_katsura:.2f}% 입니다.")
print("-" * 30)
