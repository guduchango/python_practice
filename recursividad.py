def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

factorial_5 = print(factorial(20))


def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
number = 6

print(fibonnacci(number))
