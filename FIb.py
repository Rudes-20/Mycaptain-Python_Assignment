a, b = 0, 1
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib = [a, b]
i = 2
while i < n:
    a, b = b, a + b
    fib.append(b)
    i += 1
print(fib)
