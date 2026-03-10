pw = input("비밀번호 입력: ")

lengChk = "X"
upperChk = "X"
lowerChk = "X"
digitChk = "X"
symbolChk = "X"
level = 0

if len(pw) >= 8:
    lengChk = "✔"
    level += 1

for ch in pw:
    if ch >= 'A' and ch <= 'Z' and upperChk == "X":
        upperChk = "✔"
        level += 1

    if ch >= 'a' and ch <= 'z' and lowerChk == "X":
        lowerChk = "✔"
        level += 1

    if ch >= '0' and ch <= '9' and digitChk == "X":
        digitChk = "✔"
        level += 1

    if ch in "!@#$%^&*()_+-=`,.;:'" and symbolChk == "X":
        symbolChk = "✔"
        level += 1

print(f"[{lengChk}] 길이 8자 이상")
print(f"[{upperChk}] 대문자 포함")
print(f"[{lowerChk}] 소문자 포함")
print(f"[{digitChk}] 숫자 포함")
print(f"[{symbolChk}] 특수문자 포함")

if level == 5:
    grade = "매우 강함"
else:
    grade = "취약"

print(f"비밀번호 강도: {grade}")