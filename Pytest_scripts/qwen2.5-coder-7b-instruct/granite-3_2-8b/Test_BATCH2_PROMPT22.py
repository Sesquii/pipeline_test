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

# ===== GENERATED TESTS =====
```python
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

# test_main.py
import pytest
from typing import Callable

def test_func1(capsys):
    """
    Test the func1 function from module1.
    """
    func1 = pytest.importorskip('module1').func1
    func1()
    captured = capsys.readouterr()
    assert captured.out == "Function 1 from module1\n"

def test_complex_init():
    """
    Test the complex_init function in main.py.
    """
    complex_init = pytest.importorskip('main').complex_init
    complex_init()

def test_module2_func2(capsys):
    """
    Test the func2 function from module2.
    """
    func2 = pytest.importorskip('module2').func2
    func2()
    captured = capsys.readouterr()
    assert captured.out == "Function 2 from module2\n"

def test_module1_func1(capsys):
    """
    Test the func1 function from module1.
    """
    func1 = pytest.importorskip('module1').func1
    func1()
    captured = capsys.readouterr()
    assert captured.out == "Function 1 from module1\n"

def test_module2_func2_with_complex_init(capsys):
    """
    Test the func2 function from module2 with complex_init.
    """
    pytest.importorskip('main').complex_init()
    func2 = pytest.importorskip('module2').func2
    func2()
    captured = capsys.readouterr()
    assert captured.out == "Function 2 from module2\n"

def test_module1_func1_with_complex_init(capsys):
    """
    Test the func1 function from module1 with complex_init.
    """
    pytest.importorskip('main').complex_init()
    func1 = pytest.importorskip('module1').func1
    func1()
    captured = capsys.readouterr()
    assert captured.out == "Function 1 from module1\n"
```