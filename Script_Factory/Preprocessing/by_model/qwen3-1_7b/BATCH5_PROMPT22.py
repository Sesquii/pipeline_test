```python
def tesseract_string(input_string):
    def generate_primes(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                sieve[i*i : limit+1 : i] = [False] * len(sieve[i*i : limit+1 : i])
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        return primes
    primes = generate_primes(100000)
    result = []
    for i, c in enumerate(input_string):
        asc = ord(c)
        p = primes[i] if i < len(primes) else 2
        new_asc = (asc ** p + i) % 256
        result.append(chr(new_asc))
    return ''.join(result)

if __name__ == "__main__":
    input_str = "example"
    output = tesseract_string(input_str)
    print(output)