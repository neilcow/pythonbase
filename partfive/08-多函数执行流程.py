number = 0


def test1():
    global number
    number = 100


def test2():
    print(number)


test1()
test2()