# 파이썬 함수 특징
# 생성 : def 함수명():
# 실행법 : 함수명()
# 매개변수 값을 전달할 때 : 함수명(매개변수)
# 파이썬 지역 & 전역 변수 특징
    # • def 안 → 지역변수
    # Scope란 변수를 사용할 수 있는 범위를 말한다
    # • 파이썬은 블록(if, for 등)이 아니라 함수(def) 기준으로 스코프(Scope)가 나뉜다.
    # • def 밖 → 전역변수
    # • if / for / while → 새로운 지역 스코프를 만들지 않음
# 함수에서 값을 return 받을때 여러개인 경우 튜플 사용
# 함수 내에서 외부정의된 전역변수 사용시 global ~사용

# 매개변수(name) 사용 호출
def print_address(name):
    print("종로구")
    print("파이썬 건물")
    print("302호")
    print(name)

print_address("홍길동")

# 함수 값 반환하기
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum
result = get_sum(1,10)
print(result)

# 원 반지름 입력받아서 결과내기
def cal_area(r, p):
    area = pi * radius ** 2
    return area
# print(area) => 함수 내 정의한 지역변수라 함수 호출을 통해 접근가능
pi = 3.14
radius = float(input("반지름: "))
cal_result = cal_area(radius, pi)
print(cal_result)