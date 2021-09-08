"""

THIS IS USED FOR ENCRIPTING AND DECRIPTING SHA256

"""

import math

# ENCRIPTION

def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def right_rotate(n, bits):
    return (n >> bits) | (n << (32 - bits)) & 0xFFFFFFFF


def mod_add(*args):
    return sum(args) % 2**32

def sti(string: str):
    return int(string, 2)


def ch(x, y, z):
    return (x & y) ^ ((~x) & z)


def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def Sigma0(x):
    return (right_rotate(x, 2)) ^ (right_rotate(x, 13)) ^ (right_rotate(x, 22))


def Sigma1(x):
    return (right_rotate(x, 6)) ^ (right_rotate(x, 11)) ^ (right_rotate(x, 25))


def smallsigma0(x):
    return (right_rotate(x, 7)) ^ (right_rotate(x, 18)) ^ (x >> 3)


def smallsigma1(x):
    return (right_rotate(x, 17)) ^ (right_rotate(x, 19)) ^ (x >> 10)

def encript():
    HASH = [int(math.modf(math.sqrt(num))[0]*(1 << 32)) for num in range(2, 20) if is_prime(num)] # Inital Hash Values

    CONSTANTS = [int(math.modf(num**(1/3))[0]*(1 << 32)) for num in range(2, 312) if is_prime(num)] # Round Constraints

    Message = input("Enter a Message to encript it (Using SHA256): ");  
    Message = ''.join(format(ord(letter), '08b') for letter in Message) + '1' + '0'*(512 - ((len(Message)*8+65) % 512)) + format(len(Message)*8, '064b') # Putting Message in the Block of 512 bits

    for Block in range(0, len(Message), 512):
        a = HASH[0]
        b = HASH[1]
        c = HASH[2]
        d = HASH[3]
        e = HASH[4]
        f = HASH[5]
        g = HASH[6]
        h = HASH[7]
        Block = Message[Block:Block+512]
        w = [sti(Block[x:x+32]) for x in range(0, 512, 32)]
        for j in range(16, 64):
            w.append(mod_add(smallsigma1(w[j - 2]), w[j - 7], smallsigma0(w[j - 15]), w[j - 16]))
        for loop in range(0, 64):
            temp1 = mod_add(h, ch(e, f, g), Sigma1(e), w[loop], CONSTANTS[loop])
            temp2 = mod_add(maj(a, b, c), Sigma0(a))
            h = g
            g = f
            f = e
            e = mod_add(d, temp1)
            d = c
            c = b
            b = a
            a = mod_add(temp1, temp2)
        for x in range(8):
            HASH[x] = mod_add(HASH[x], list([a, b, c, d, e, f, g, h])[x])

    Result = ''.join(format(HASH[x], '08x') for x in range(8))
    print("Your Encripted Message is:", Result.upper())
    return 0

# DECRIPTION

"""
def make_next_guess(guess):
    carry = 1
    next_guess = guess

    for i in range(len(guess)):
        cur_char = ord(guess[i]) + carry
        if cur_char > ord('z'):
            cur_char = ord('A')
            carry = 1
        else:
            carry = 0

        next_guess = next_guess[:i] + chr(cur_char) + guess[i + 1:]
        if carry == 0:
             break

    if carry == 1:
        next_guess += 'A'

    return next_guess

"""
def decript():
    """
    guess = 'A'
    for _ in range(58 ** 14):
        if hash_password(guess) == secure_password:
            print(guess)
            break
        guess = make_next_guess(guess)
        """
    print("This still does not work :( . So it is like I have not even done anything :( .. ") 
    return -1
