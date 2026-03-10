# 해당 배열 갯수만큼 반복
for i in [1,2,3,4,5]:
    print("2 *", i, "=" , 2*i)

# for 변수 in range(종료값) => 변수가 0부터 종료값-1 까지 반복
for i in range(5):
    print(f"{i} 반복") # 문자 + 값 할때는 f-string

# for 변수 in range(초기값, 종료값, 증감값)
# 증감값 생략시 1
for i in range(1,6,1):
    print(i)
    print(type(i))