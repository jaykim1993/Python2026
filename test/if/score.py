name = input("이름 : ")
korean = int(input("국어 : "))
english = int(input("수학 : "))
math = int(input("영어 : "))
total = korean + english + math
avrScore = total/3
grade = ""
if avrScore >= 90:
    grade = "A"
elif avrScore < 90 and avrScore >= 80:
    grade = "B"
elif avrScore < 80 and avrScore >= 70:
    grade = "C"
elif avrScore <70 and avrScore >= 60:
    grade = "D"
elif avrScore < 60 and avrScore >= 0:
    grade ="F"

print("-"*60)
print(f"이름 : {name:>5}")
print(f"국어 : {korean:>5}점")
print(f"영어 : {english:>5}점")
print(f"수학 : {math:>5}점")
print("-"*60)
print(f"총점 : {total:>5}점")
print(f"평균 : {avrScore:>5.2f}점")
print(f"학점 : {grade:>6}")