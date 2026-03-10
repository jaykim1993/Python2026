#다중 for문 사용해서 구구단 2단 ~ 9단 출력
for i in range(2,10):
    print(f"-----{i}단 시작-----")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
    print()

# 정수 입력 후 정수! 돌리기
n = int(input("정수를 입력하시오: "))
result = 1
for i in range(n, 0, -1):
    result = result * i
print(f"{n}! = {result}")