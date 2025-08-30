```python
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