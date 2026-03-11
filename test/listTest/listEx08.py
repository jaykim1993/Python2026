subjects = [
    {"subject":"Python 프로그래밍", "score": 92, "credit":3},
    {"subject":"SpringBoot 개발\t", "score": 88, "credit":3},
    {"subject":"React 프론트엔드", "score": 76, "credit":2},
    {"subject":"데이터베이스\t", "score": 95, "credit":3},
    {"subject":"알고리즘\t", "score": 68, "credit":2},
]

point = 0.0 # 과목별 학점
grade = "" # 과목별 등급
gpa = 0 # 과목별 gpa
GPA = 0 # 전체 GPA
credits = 0 # 총 학점

gradeDistribution = {} # 등급분포표

print("================= 성적표 ================================")
print(f"{'과목명'}\t\t\t {'점수'}\t {'등급'}\t {'평점'}\t {'이수학점'}")
print("---------------------------------------------------------")

for subject in subjects:
    if subject["score"] >= 95:
        point = 4.5
        grade = "A+"
    elif 90 <= subject["score"] < 95:
        point = 4.0
        grade = "A"
    elif 85 <= subject["score"] < 90:
        point = 3.5
        grade = "B+"
    elif 80 <= subject["score"] < 85:
        point = 3.0
        grade = "B"
    elif 75 <= subject["score"] < 80:
        point = 2.5
        grade = "C+"
    elif 70 <= subject["score"] < 75:
        point = 2.0
        grade = "C"
    elif 60 <= subject["score"] < 70:
        point = 1.0
        grade = "D"
    else :
        point = 0
        grade = "F"
    
    # 과목별 값 업데이트
    subject["grade"] = grade
    subject["point"] = point
    gpa += point*subject["credit"]
    credits += subject["credit"]

    # 학점 분포표에 업데이트 하기
    if grade not in gradeDistribution:
        gradeDistribution[grade] = 1
    else:
        gradeDistribution[grade] += 1

    # 과목별 필드 출력
    print(f"{subject['subject']}\t {subject["score"]}점\t {subject["grade"]}\t {subject["point"]}\t {subject['credit']}학점")
    


# 전체 총계 출력
GPA = gpa/credits
print("=========================================================")
print(f"\nGPA: {GPA:.2f} / 4.50 (총 {credits}학점)")
print(f"학점분포: {gradeDistribution}")
