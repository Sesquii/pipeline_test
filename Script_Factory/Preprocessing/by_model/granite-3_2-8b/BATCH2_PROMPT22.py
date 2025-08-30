# module1.py
def func1():
    print("Function 1 from module1")


def complex_init():
    global func2
    import module2
    func2 = module2.func2

# module2.py
def func2():
    print("Function 2 from module2")


def complex_init():
    global func1
    import module1
    module1.complex_init()
    func1 = module1.func1

# main.py
def complex_init():
    import module1
    import module2

    module1.complex_init()
    module2.complex_init()


if __name__ == "__main__":
    complex_init()
    module1.func1()
    module2.func2()