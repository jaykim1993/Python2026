# 파이썬 조건문
# if : 과 들여쓰기가 핵심!
# if 조건식 :
#   print("출력문")
# else :
#   print("출력문")

score = int(input("점수입력: "))
if score >= 90 :
    print("합격")
else :
    print("불합격")

# 한줄로 쓰기 
# 조건부 표현식(Ternary Operator)
score2 = int(input("점수입력: "))
message = "합격" if score2 >= 60 else "불합격"
print(message)