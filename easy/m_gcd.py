# To find greatest common denominator/divisor:
# divide bigger number by smaller, find the remainder
# now remainder becomes the smaller number and previously smaller number becomes the bigger one
# repeat the process until remainder is 0. The divisor you get when the remainder is 0 is the gcd

def gcd(a, b):
    while(b):
        rem = a % b
        a = b
        b = rem

    return a

a = int(input('enter num 1: '))
b = int(input('enter num 2: '))
print('gcd is: ', gcd(a, b))