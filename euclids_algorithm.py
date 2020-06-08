# Euclid's Algorithm
# Find the greatest common denominator of two integers

def findGCD(int_1, int_2):
    if int_1 > int_2:
        remainder = int_1 % int_2
        while remainder != 0:
            int_1 = int_2
            int_2 = remainder
            remainder = int_1 % int_2
        print(int_2)
    else:
        remainder = int_2 % int_1
        while remainder != 0:
            int_2 = int_1
            int_1 = remainder
            remainder = int_2 % int_1
        print(int_1)

findGCD(400, 500)