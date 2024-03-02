import time
import numpy as np

def number_asker(): # Asks for two prime numbers that fit the criteria
    print('Larger prime numbers are recommended for better security\n')
    while True:
        try:
            p = int(input('Give a prime number: '))
            if is_prime(p):
                break
            else:
                print('The number is not prime')
                continue
        except ValueError:
            print('The number is not prime')
            continue

    while True:
        try:
            q = int(input('Give a second prime number: '))
            print()
            if is_prime(q) and p != q and p * q > 100:
                break
            elif not is_prime(q):
                print('The number is not prime. Try again.')
                continue
            elif p == q:
                print('The number is the same as the first number. Try again.')
                continue
            elif p * q < 100:
                print('The product of the numbers is too small. Try again.')
                continue

        except ValueError:
            print('The number is not prime')
            continue

    return p, q

def is_prime(n: int) -> bool:
    start = time.time()

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Tarkistetaan pienimmät alkuluvut
    small_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False

    # Tarkistetaan suuremmat luvut aloittaen luvusta 101 ja jatkaen kuuden välein
    i = 101
    while i * i <= n:
        if n % i == 0 or n % (i + 6) == 0:
            return False
        i += 6

    print('Time to check if the number is prime:', time.time() - start)
    return True

# Greatest common divisor
def gcd(a: int, b: int) -> int: 
    gcd_start = time.time()
    while b:
        a, b = b, a % b
    print('Time to calculate the greatest common divisor:', time.time() - gcd_start)
    return a

# checks if two numbers are coprime and returns a boolean value
def are_coprime(a: int, b: int) -> bool:
    return gcd(a,b) == 1 

# calculates the modular multiplicative inverse of a number `a` modulo `m`
def modinv(a: int, m: int) -> int:
    modinv_start = time.time()
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    print('Time to calculate the modular multiplicative inverse:', time.time() - modinv_start)
    return x1 + m0 if x1 < 0 else x1

# calculates the public and private keys e and d
def get_keys(phi: int) -> tuple[int, int]:
    get_keys_start = time.time()
    e = d = 0
    for i in range(2, phi):
        if are_coprime(i, phi):
            e = i
            break
    d = modinv(e, phi)
    print('Time to calculate the public and private keys:', time.time() - get_keys_start)
    return e, d

# encrypts the message using the public key
def encrypt(message: str, e: int, n: int, characters: list) -> str:
    return ' '.join([str(pow(characters.index(ch) + 1, e, n)) for ch in message])

# decrypts the message using the private key
def decrypt(encrypted_message: str, d: int, n: int, characters: list) -> str:
    return ''.join([characters[pow(int(num), d, n) - 1] for num in encrypted_message.split()])
