def func():
    print("function part 1")

    x = yield
    print(x)
    print("function parte 2")

    a = yield
    print(a)
    print("Function parte 3")


try:
    n = func()

    next(n)

    n.send(6)

    n.send(12)

except StopIteration as e:
    pass
