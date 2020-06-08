# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(int_1, int_2):
    remainder = int_1 % int_2
    while remainder != 0:
        int_1 = int_2
        int_2 = remainder
        remainder = int_1 % int_2
    return int_2


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
