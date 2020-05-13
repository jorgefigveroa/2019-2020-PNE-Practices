# -- Describe a function that states the fibonacci sequence.
# -- The main console should describe the 5th, 10th and 15th terms of the fibonacci sequence.


def fibon(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n)


def fibonacci(n):
    fibo1 = 0
    fibo2 = 1
    count = 0
    for i in range(0, n-1):
        count = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = count
    return count


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))
