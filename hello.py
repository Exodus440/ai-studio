def greeting(name, language="en"):
    if language == "ko":
        return f"안녕하세요, {name}님!"
    else:
        return f"Hello, {name}!"


print(greeting("Hong Gildong"))
print(greeting("홍길동", "ko"))

