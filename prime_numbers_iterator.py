class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.i = 2
        self.prime_numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.n:
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
            self.i += 1
        else:
            raise StopIteration


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)
