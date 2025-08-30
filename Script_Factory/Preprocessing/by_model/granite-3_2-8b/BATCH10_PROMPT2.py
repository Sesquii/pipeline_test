#!/usr/bin/env python3

import psutil
from random import choice
from haikus import get_haiku  # You'll need to install this library using pip: pip install haikus


def memory_to_haiku():
    memory = dict(psutil.virtual_memory()._asdict())
    free = f"{memory['free'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places
    used = f"{memory['used'] / (1024**3):.2f}"  # Convert bytes to GB, format to 2 decimal places

    lines = [
        f"Memory's vast expanse,",
        f"{choice(['sparse', 'crammed', 'empty', 'packed'])} with {free}.",
        f"A world within my grasp."
    ]

    return "\n".join(lines)


def main():
    haiku = memory_to_haiku()
    print(haiku)


if __name__ == "__main__":
    main()