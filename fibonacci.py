class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result


fib_iter = FibonacciIterator(10)

for num in fib_iter:
    print(num)

fib_iter = FibonacciIterator(7)
iterator = iter(fib_iter)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator tugadi")
