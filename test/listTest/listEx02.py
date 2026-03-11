member = {
'name' : '김파이썬',
'email' : 'python@example.com',
'age' : 28,
'grade' : 'GOLD'
}

ageStr = ""
phoneStr = ""

if member['age'] < 20:
    ageStr = "주니어"
elif 20 <= member['age'] <= 39:
    ageStr = "일반"
elif 40 <= member['age']:
    ageStr = "시니어"

print("=== 회원 정보 ===")
for key in member.keys():
    print(f"\t{key}: {member[key]}")
    if "phone" in member.keys():
        phoneStr = "등록"
    else :
        phoneStr = "미등록"

print(f"\n연령 구간 : {ageStr}")
print(f"전화번호: {phoneStr}")

