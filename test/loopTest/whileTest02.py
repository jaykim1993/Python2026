# 1부터 10까지의 합 구하기
i = 1
sum = 0
while i <=10:
    sum += i
    i += 1
print(f"1부터 10 까지의 합 : {sum}")

# 다중 while문 이용해서
# 구구단 2단 ~ 9단 출력
dan = 2
while dan <= 9: 
    value = 1
    print(f"----{dan}단----")
    while value <= 9:
        print(f"{dan} x {value} = {dan*value}")
        value += 1
    dan += 1
    