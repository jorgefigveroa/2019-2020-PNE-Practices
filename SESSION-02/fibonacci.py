# -- FIBONACCI SEQUENCE EXCERCISE
# -- WITHOUT CREATING A FUNCTION THE 11 FIRST NUMBERS.

fibo1 = 0
fibo2 = 1
for i in range(0, 10):
    if i == 0:
        print("0", end=" ")
    if i == 1:
        print("1", end=" ")
    else:
        count = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = count
        print(count, end=" ")
