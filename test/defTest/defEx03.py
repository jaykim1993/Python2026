member_data = [
{"name": "김철수", "age": 20},
{"name": "이영희", "age": 25},
{"name": "박민수", "age": 18}
]
overTwenty = []
def filter_members():
    global member_data
    global overTwenty
    for member in member_data:
        if member["age"] >= 20:
            overTwenty.append(member["name"])
    return
filter_members()

print("20세 이상 회원: ", overTwenty)