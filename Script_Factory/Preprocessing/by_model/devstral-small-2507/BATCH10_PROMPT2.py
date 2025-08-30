# BATCH10_PROMPT2_Devstral.py

import os
import psutil

def get_memory_info():
    """Get current system memory usage information."""
    mem = psutil.virtual_memory()
    total_gb = round(mem.total / (1024 ** 3), 2)
    available_gb = round(mem.available / (1024 ** 3), 2)
    used_gb = round(mem.used / (1024 ** 3), 2)
    percent_used = mem.percent

    return total_gb, available_gb, used_gb, percent_used

def generate_haiku(total, available, used, percent):
    """Generate a haiku based on memory usage."""
    lines = []

    # First line: Total memory
    if total < 8:
        lines.append("Memory is quite sparse")
    elif total < 16:
        lines.append("Memory is modest")
    else:
        lines.append("Memory is abundant")

    # Second line: Available memory
    if available < 2:
        lines.append("Little space remains")
    elif available < 4:
        lines.append("Some room still exists")
    else:
        lines.append("Plenty of free space")

    # Third line: Usage percentage
    if percent < 50:
        lines.append("System breathes easy")
    elif percent < 80:
        lines.append("Working quite hard")
    else:
        lines.append("Pushing its limits")

    return "\n".join(lines)

def main():
    """Main entry point of the program."""
    # Get memory information
    total, available, used, percent = get_memory_info()

    # Generate haiku
    haiku = generate_haiku(total, available, used, percent)

    # Print the haiku
    print("System Memory Haiku:")
    print(haiku)
    print(f"\nMemory Stats: {total}GB total, {available}GB free, {used}GB used, {percent}% usage")

if __name__ == "__main__":
    main()