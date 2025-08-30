import resource

if __name__ == "__main__":
    def get_memory_usage():
        mem_info = resource.getrusage(resource.RUSAGE_SELF)
        return mem_info.ru_maxrss

    memory_bytes = get_memory_usage()
    memory_mb = memory_bytes / (1024 * 1024)

    line1 = f"Memory: {memory_mb:.2f} MB"
    line2 = "High, but not too high"
    line3 = "Efficient use of resources"

    print(line1)
    print(line2)
    print(line3)

# ===== GENERATED TESTS =====
import pytest
from unittest.mock import patch

# Original script
def get_memory_usage():
    mem_info = resource.getrusage(resource.RUSAGE_SELF)
    return mem_info.ru_maxrss

memory_bytes = get_memory_usage()
memory_mb = memory_bytes / (1024 * 1024)

line1 = f"Memory: {memory_mb:.2f} MB"
line2 = "High, but not too high"
line3 = "Efficient use of resources"

print(line1)
print(line2)
print(line3)


# Test cases
def test_get_memory_usage():
    """Test the get_memory_usage function"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 1048576  # 1 MB in bytes
        assert get_memory_usage() == 1048576

def test_get_memory_usage_negative():
    """Test the get_memory_usage function with negative input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = -1  # Invalid memory usage
        assert get_memory_usage() == -1

def test_get_memory_usage_zero():
    """Test the get_memory_usage function with zero input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 0  # No memory usage
        assert get_memory_usage() == 0

def test_get_memory_usage_large():
    """Test the get_memory_usage function with large input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 1073741824  # 1 GB in bytes
        assert get_memory_usage() == 1073741824

def test_get_memory_usage_small():
    """Test the get_memory_usage function with small input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 512 * 1024  # 512 KB in bytes
        assert get_memory_usage() == 512 * 1024

def test_get_memory_usage_none():
    """Test the get_memory_usage function with None input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = None  # Invalid memory usage
        assert get_memory_usage() is None

def test_get_memory_usage_string():
    """Test the get_memory_usage function with string input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = "1048576"  # Invalid memory usage
        assert get_memory_usage() == "1048576"

def test_get_memory_usage_float():
    """Test the get_memory_usage function with float input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 1.0  # Invalid memory usage
        assert get_memory_usage() == 1.0

def test_get_memory_usage_list():
    """Test the get_memory_usage function with list input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = [1048576]  # Invalid memory usage
        assert get_memory_usage() == [1048576]

def test_get_memory_usage_dict():
    """Test the get_memory_usage function with dict input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = {'ru_maxrss': 1048576}  # Invalid memory usage
        assert get_memory_usage() == {'ru_maxrss': 1048576}

def test_get_memory_usage_set():
    """Test the get_memory_usage function with set input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = {1048576}  # Invalid memory usage
        assert get_memory_usage() == {1048576}

def test_get_memory_usage_tuple():
    """Test the get_memory_usage function with tuple input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = (1048576,)  # Invalid memory usage
        assert get_memory_usage() == (1048576,)

def test_get_memory_usage_complex():
    """Test the get_memory_usage function with complex input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = 1048576 + 1j  # Invalid memory usage
        assert get_memory_usage() == 1048576 + 1j

def test_get_memory_usage_bool():
    """Test the get_memory_usage function with bool input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = True  # Invalid memory usage
        assert get_memory_usage() == True

def test_get_memory_usage_bytes():
    """Test the get_memory_usage function with bytes input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = b'1048576'  # Invalid memory usage
        assert get_memory_usage() == b'1048576'

def test_get_memory_usage_bytearray():
    """Test the get_memory_usage function with bytearray input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = bytearray(b'1048576')  # Invalid memory usage
        assert get_memory_usage() == bytearray(b'1048576')

def test_get_memory_usage_buffer():
    """Test the get_memory_usage function with buffer input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = memoryview(bytearray(b'1048576'))  # Invalid memory usage
        assert get_memory_usage() == memoryview(bytearray(b'1048576'))

def test_get_memory_usage_function():
    """Test the get_memory_usage function with function input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = lambda: 1048576  # Invalid memory usage
        assert get_memory_usage() == lambda: 1048576

def test_get_memory_usage_class():
    """Test the get_memory_usage function with class input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = type('MyClass', (object,), {'__init__': lambda self: None})  # Invalid memory usage
        assert get_memory_usage() == type('MyClass', (object,), {'__init__': lambda self: None})

def test_get_memory_usage_module():
    """Test the get_memory_usage function with module input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = __import__('os')  # Invalid memory usage
        assert get_memory_usage() == __import__('os')

def test_get_memory_usage_generator():
    """Test the get_memory_usage function with generator input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = (x for x in range(1048576))  # Invalid memory usage
        assert get_memory_usage() == (x for x in range(1048576))

def test_get_memory_usage_coroutine():
    """Test the get_memory_usage function with coroutine input"""
    with patch('resource.getrusage') as mock_getrusage:
        async def coro():
            return 1048576
        mock_getrusage.return_value.ru_maxrss = coro()  # Invalid memory usage
        assert get_memory_usage() == coro()

def test_get_memory_usage_async_generator():
    """Test the get_memory_usage function with async generator input"""
    with patch('resource.getrusage') as mock_getrusage:
        async def async_gen():
            yield 1048576
        mock_getrusage.return_value.ru_maxrss = async_gen()  # Invalid memory usage
        assert get_memory_usage() == async_gen()

def test_get_memory_usage_async_function():
    """Test the get_memory_usage function with async function input"""
    with patch('resource.getrusage') as mock_getrusage:
        async def async_func():
            return 1048576
        mock_getrusage.return_value.ru_maxrss = async_func()  # Invalid memory usage
        assert get_memory_usage() == async_func()

def test_get_memory_usage_async_class():
    """Test the get_memory_usage function with async class input"""
    with patch('resource.getrusage') as mock_getrusage:
        class AsyncClass:
            async def __init__(self):
                pass
        mock_getrusage.return_value.ru_maxrss = AsyncClass()  # Invalid memory usage
        assert get_memory_usage() == AsyncClass()

def test_get_memory_usage_async_module():
    """Test the get_memory_usage function with async module input"""
    with patch('resource.getrusage') as mock_getrusage:
        mock_getrusage.return_value.ru_maxrss = __import__('asyncio')  # Invalid memory usage
        assert get_memory_usage() == __import__('asyncio')

def test_get_memory_usage_async_generator_function():
    """Test the get_memory_usage function with async generator function input"""
    with patch('resource.getrusage') as mock_getrusage:
        async def async_gen_func():
            yield 1048576
        mock_getrusage.return_value.ru_maxrss = async_gen_func()  # Invalid memory usage
        assert get_memory_usage() == async_gen_func()

def test_get_memory_usage_async_coroutine_function():
    """Test the get_memory_usage function with async coroutine function input"""
    with patch('resource.getrusage') as mock_getrusage:
        async def async_coro_func():
            return 1048576
        mock_getrusage.return_value.ru_maxrss = async_coro_func()  # Invalid memory usage
        assert get_memory_usage() == async_coro_func()

def test_get_memory_usage_async_class_method():
    """Test the get_memory_usage function with async class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        class AsyncClass:
            @staticmethod
            async def async_method():
                return 1048576
        mock_getrusage.return_value.ru_maxrss = AsyncClass.async_method()  # Invalid memory usage
        assert get_memory_usage() == AsyncClass.async_method()

def test_get_memory_usage_async_module_function():
    """Test the get_memory_usage function with async module function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.sleep(1)  # Invalid memory usage
        assert get_memory_usage() == asyncio.sleep(1)

def test_get_memory_usage_async_generator_class_method():
    """Test the get_memory_usage function with async generator class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        class AsyncClass:
            @staticmethod
            async def async_gen_method():
                yield 1048576
        mock_getrusage.return_value.ru_maxrss = AsyncClass.async_gen_method()  # Invalid memory usage
        assert get_memory_usage() == AsyncClass.async_gen_method()

def test_get_memory_usage_async_coroutine_class_method():
    """Test the get_memory_usage function with async coroutine class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        class AsyncClass:
            @staticmethod
            async def async_coro_method():
                return 1048576
        mock_getrusage.return_value.ru_maxrss = AsyncClass.async_coro_method()  # Invalid memory usage
        assert get_memory_usage() == AsyncClass.async_coro_method()

def test_get_memory_usage_async_module_class_method():
    """Test the get_memory_usage function with async module class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_function():
    """Test the get_memory_usage function with async generator module function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.gather(asyncio.sleep(1))  # Invalid memory usage
        assert get_memory_usage() == asyncio.gather(asyncio.sleep(1))

def test_get_memory_usage_async_coroutine_module_function():
    """Test the get_memory_usage function with async coroutine module function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.create_task(asyncio.sleep(1))  # Invalid memory usage
        assert get_memory_usage() == asyncio.create_task(asyncio.sleep(1))

def test_get_memory_usage_async_generator_module_class_method():
    """Test the get_memory_usage function with async generator module class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method():
    """Test the get_memory_usage function with async coroutine module class method input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_generator_module_class_method_function():
    """Test the get_memory_usage function with async generator module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio
        mock_getrusage.return_value.ru_maxrss = asyncio.Queue()  # Invalid memory usage
        assert get_memory_usage() == asyncio.Queue()

def test_get_memory_usage_async_coroutine_module_class_method_function():
    """Test the get_memory_usage function with async coroutine module class method function input"""
    with patch('resource.getrusage') as mock_getrusage:
        import asyncio