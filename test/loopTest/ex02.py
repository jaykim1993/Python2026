# 배경: React 프론트엔드에서API 요청 전 입력값을 검증하는 로직을 구현합니다.
    # 요구사항
        # - 회원가입 시 아이디, 비밀번호, 이메일을 순서대로 입력받아 유효성을 검사하세요.
        # - 아이디: 4자 이상12자 이하(len() 사용 가능)
        # - 비밀번호: 8자 이상, 숫자 포함 여부는 직접 확인
        # - 이메일: 반드시 '@' 문자 포함 여부 확인(in 연산자 사용)
        # - 각 항목이 조건 불충족 시 다시 입력 요청(while 반복)
        # - 모든 항목 통과 시'유효성 검사 통과! API 요청을 전송합니다.' 출력
    # <출력 결과>
        # 아이디 입력(4~12자): ab
        # 아이디는4자 이상12자 이하여야 합니다. 다시 입력하세요.
        # 아이디 입력(4~12자): hong123
        # 비밀번호 입력(8자 이상, 숫자 포함): abcdefg
        # 비밀번호는8자 이상이어야 합니다. 다시 입력하세요.
        # 유효성 검사 통과! API 요청을 전송합니다.

# ID 유효성 검사
while True:
    inputID = input("아이디 입력 (4~12자): ")
    if 4 <= len(inputID) <= 12:
        break
    else:
        print("아이디는 4자 이상 12자 이하여야 합니다. 다시 입력하세요.")
# PW 유효성 검사
while True:
    inputPW = input("비밀번호 입력 (8자 이상, 숫자 포함): ")
    if len(inputPW) >= 8 and not inputPW.isalpha():
        break
    else:
        print("비밀번호는 8자 이상, 숫자를 포함하여야 합니다. 다시 입력하세요.")
# Email 유효성 검사
while True:
    inputEmail = input("이메일 입력 (@ 포함+): ")
    if "@" in inputEmail:
        break
    else:
        print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")

print("유효성 검사 통과! API 요청을 전송합니다.")


s = "abc123"

# 숫자만인지
print(s.isdigit())   # False

# 문자만인지
print(s.isalpha())   # False

# 숫자 또는 문자만(공백 없음)인지
print(s.isalnum())   # True

# 10진수(0-9)만인지
print(s.isdecimal()) # False