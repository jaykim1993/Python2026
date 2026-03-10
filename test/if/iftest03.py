# 점수를 입력받아서 0이면 0이다. 0보다 크면 양수이다. 아니면 음수이다.
score = int(input("점수입력: "))

# (참일 때 값) if (조건) else (거짓일 때 다시 if문...)
if score > 0:
    msg = "양수이다"
elif score == 0:
    msg = "0이다"
else:
    msg = "음수이다"

print(msg)