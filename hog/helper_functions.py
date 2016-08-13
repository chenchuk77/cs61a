

def is_prime(number):
    loops = number
    # prime number must be 2 or more ( 1 is not prime ! ).
    if number < 2:
        return False
    # devide the number x by all numbers from 2..(x-1) check the modulo.
    for devisor in range (2, number-1):
        if number % devisor == 0:
            return False
    # no success devision found -> its a prime number.
    return True


def next_prime(number):
    # starting condition: input is a prime number
    assert is_prime(number), "method must take a prime number."
    # try the next int until finding a prime number and returns it.
    next_prime = (number + 1)
    while True:
        if is_prime(next_prime):
            return next_prime
        next_prime +=1
    return "error"

def get_max_digit(number):
    assert number > 0 and number < 100 , "input number: x | 0 < x < 100."
    assert type(number) == int, "input number must be an integer."
    # split the number into digits and returns the biggest.
    units = number % 10
    tens = number // 10
    return units if units >= tens else tens

