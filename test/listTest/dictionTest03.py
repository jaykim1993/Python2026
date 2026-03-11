drink = {"콜라":7, "사이다":6, "우유":8, "커피":10}
# 음료수 이름을 입력하면 번호가 출력되게 작성하세요

while True:
    inputKey = input("음료를 입력하세요 (중지: 그만): ")
    if inputKey == "그만":
        print("종료됩니다.")
        break
    elif inputKey in drink:
        print(f"{inputKey}의 번호는 {drink[inputKey]}번입니다.")
    else:
        print(f"{inputKey}은(는) 메뉴에 없습니다.")