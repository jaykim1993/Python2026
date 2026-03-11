response = {
'code' : 200,
'message': 'success',
'data' 
    : [
    {'userId': 'user01', 'name': '이자바', 'score': 95},
    {'userId': 'user02', 'name': '박리액트', 'score': 82},
    {'userId': 'user03', 'name': '최스프링', 'score': 91},
    {'userId': 'user04', 'name': '정마이바티스', 'score': 78}
    ]
}

if response['code'] == 200:
    students = response['data']
    highScoreStudents = []

    print("=== 전체 성적 ===")
    for student in students:
        print(f"{student['name']} ({student['userId']}): {student['score']}점")
        if student['score'] >= 90:
            highScoreStudents.append(student)

    print(f"\n=== 우수 수강생 (90점 이상): {len(highScoreStudents)}명")
    for student in highScoreStudents:
        print(f"★ {student['name']}: {student['score']}점")