def get_prime_number(n):
    def prime_number(func):
        def prime_numbers_generator(*args, **kwargs):
            num = 2
            while num < n:
                for prime in prime_numbers:
                    if num % prime == 0:
                        break
                else:
                    prime_numbers.append(num)
                    check = func(*args, **kwargs)
                    yield num, check
                num += 1
        return prime_numbers_generator
    return prime_number


@get_prime_number(n=10000)
def is_lucky():
    for num in prime_numbers[-1:]:
        num = str(num)
        num_list = list(map(int, num))
        n = len(num) // 2
        return sum(num_list[:n]) == sum(num_list[-n:])


@get_prime_number(n=10000)
def is_palindrome():
    for num in prime_numbers[-1:]:
        num = str(num)
        return num == num[::-1]


@get_prime_number(n=10000)
def is_fib():
    for num in prime_numbers[-1:]:
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
            if num == b:
                return True
        return False


prime_numbers = []

numbers = is_lucky()
for number, lucky in numbers:
    print(f'{number} {lucky}')

numbers = is_palindrome()
for number, palindromic in numbers:
    print(f'{number} {palindromic}')

numbers = is_fib()
for number, fib in numbers:
    print(f'{number} {fib}')