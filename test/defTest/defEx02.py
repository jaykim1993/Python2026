score = int(input("점수를 입력하세요: "))
grade = ""
def get_grade(score):
    global grade
    if score >= 90: grade = "A"
    elif score >= 80: grade = "B"
    elif score >= 80: grade = "C"
    else: grade = "F"

get_grade(score)
print(f"학생의 학점은 {grade}입니다.")