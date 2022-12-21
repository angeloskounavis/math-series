def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#if __name__ == "__main__":
n = 9
print(fibonacci(n))


def lucas(n):
    # Base cases
    if n == 0:
        return 2;
    if n == 1:
        return 1;

    # recurrence relation
    return lucas(n - 1) + lucas(n - 2);


# Driver code to test above methods
n = 9;
print(lucas(n));


def sum_series(n, num1=0, num2=1):
    if num1 == 0 and num2 == 1:
        return fibonacci(n)
    if num1 == 2 and num2 == 1:
        return lucas(n)
    else:


        return sum_series(n-1, num1, num2) + sum_series(n-2, num1, num2)

print(sum_series(9))
