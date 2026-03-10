# input ("안내 문구") : 키보드로부터 값 입력받는다.
# 단, input()으로 입력받은 모든 값은 문자열이므로,
# 계산이 필요한 정수나 실수는 반드시 형변환을 해야한다.
# => int(input("국어점수:"))
var = int(input("정수 입력: "))
var2 = int(input("정수 입력: "))
print(type(var))
print(f"합: {var+var2}")



