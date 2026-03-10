# response = "아니"
# while response == "아니":
#     response = input("엄마, 다 됐어? ")
# print("먹자")

# continue, break 사용 가능 
# 다만 return은 함수(def)를 사용해야만 가능
# boolean 값은 반드시 True, False(대문자 시작)
while True:
    response = input("엄마, 다 됐어? ")
    if response != "아니":
        break # "아니"가 아니면 반복문을 즉시 종료
print("먹자")

