# write a function to find and return all prime numbers in a given range
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): # Check divisibility up to the square root of num. num**0.5 is the same as num**(1/2).** Adding 1 to include the square root itself in the range.
        if num % i == 0:
            return False
    return True
def primeNumbersInRange(start,end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers    
start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))
print("Prime numbers in the range:", primeNumbersInRange(start,end))
