import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    user_number = int(input("Please Provide your number: "))
    is_prime = is_prime(user_number)
    if is_prime:
        print("Your number is prime.")
    else:
        print("Your number is not prime.")
