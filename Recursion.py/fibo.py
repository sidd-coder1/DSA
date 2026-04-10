def fibonacci(num):
    if num <2:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(4))
print(fibonacci(10))
# print(fibonacci(50))   #very slow due to repeated calculations of the same Fibonacci numbers.Large number
