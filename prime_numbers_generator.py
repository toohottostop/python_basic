def prime_numbers_generator(n):
    prime_numbers = []
    num = 2
    while num < n:
        for prime in prime_numbers:
            if num % prime == 0:
                break
        else:
            prime_numbers.append(num)
            yield num
        num += 1


for number in prime_numbers_generator(n=10000):
    print(f'{number}')
