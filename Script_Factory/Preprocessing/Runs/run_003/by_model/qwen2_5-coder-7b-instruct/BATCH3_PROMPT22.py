# BATCH3_PROMPT22_{{model_name}}.py

# module1.py
import module2

def function1():
    print("Function 1 called")
    function2()

def init_module1():
    print("Initializing Module 1")
    function1()

# module2.py
import module3

def function2():
    print("Function 2 called")
    function3()

def init_module2():
    print("Initializing Module 2")
    function2()

# module3.py
import module1

def function3():
    print("Function 3 called")
    function1()

def init_module3():
    print("Initializing Module 3")
    function3()

# __main__.py
if __name__ == "__main__":
    import module1
    import module2
    import module3
    
    # Initialize modules to break circular dependencies
    module1.init_module1()
    module2.init_module2()
    module3.init_module3()