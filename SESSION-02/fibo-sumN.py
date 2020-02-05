# -- We have to write a function that sums the first n terms of the fibonacci sequence


def fibosum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n)


def fibonacci(n):
    fibo1 = 0
    fibo2 = 1
    summing = 1
    for i in range(0, n - 1):
        count = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = count
        summing = summing + count
    return summing


print("Sum of the first 5 terms of the Fibonacci series: ", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series: ", fibosum(10))
