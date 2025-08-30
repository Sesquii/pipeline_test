# BATCH3_PROMPT22_Granite.py

# Module 1 - module1.py
def func1():
    return "Function 1 from module1"


# Module 2 - module2.py
def func2():
    return "Function 2 from module2"


# Module 3 - module3.py
def func3():
    return "Function 3 from module3"


# Initialization function to resolve circular dependencies
def initialize():
    import .module1 as m1
    import .module2 as m2
    import .module3 as m3

    # Setting up interdependency
    m1.func1 = lambda: f"Resolved {m2.func2} in module1"
    m2.func2 = lambda: f"Resolved {m3.func3} in module2"
    m3.func3 = lambda: f"Resolved {m1.func1} in module3"

    return m1, m2, m3


# Entry point for the script
if __name__ == "__main__":
    m1, m2, m3 = initialize()
    
    print(f"Module 1 (func1): {m1.func1()}")
    print(f"Module 2 (func2): {m2.func2()}")
    print(f"Module 3 (func3): {m3.func3()}")