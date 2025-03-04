def factorial(n: int) -> int:
    check_num(n)

    result = 1

    for i in range(2, n+1, 1):
        result *= i

    return result


def fibonacci(n: int) -> list:
    check_num(n)

    if n == 0:
        return [0]

    result = [0, 1, 1]

    while result[-1] + result[-2] < n:
        result.append(result[-1] + result[-2])

    return result


def count_ones(n: int) -> int:
    check_num(n)

    counter = 0
    num = n

    while num > 0:
        if num & 1 == 1:
            counter += 1

        num >>= 1

    return counter


def is_palindrome(x: int) -> bool:
    if not isinstance(x, int):
        raise TypeError("")

    if x < 0:
        return False

    origin = x
    reverse = 0

    while x > 0:
        remainder = x % 10
        reverse = reverse*10 + remainder

        x //= 10

    return reverse == origin


def check_num(n):
    if not isinstance(n, int):
        raise TypeError("")

    if n < 0:
        raise ValueError("")

