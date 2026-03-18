# 디폴트 매개변수(default argument)
# = 매개변수 기본값을 가질 수 있다.
def greet(name, msg="How's it going?"):
    print(f"Hey, {name}! {msg}")

greet("Tommy")
greet("Tommy", "Long time no see!")