## Find even, odd and prime numbers in a list ##
# Objective: given a list of integer numbers, determine even, odd and prime numbers

# 1) Input

list = [1, 5, 10, 7, 52, 2, 21, 111, 11]

# 2) Output

# 2.1) Definition of even and odd numbers
even = [num for num in sorted(list) if num % 2 == 0] # num is even
odd = [num for num in sorted(list) if num % 2 != 0] # num is odd

# 2.2) Definition of prime numbers
prime = []

for num in sorted(list):
    div = 0

    for j in range(1, num):
        if num % j == 0:
            div += 1
        elif num % j != 0:
            div = div

    if div == 1:
        prime.append(num) # num is prime only if div = 1

# 2.3) Results
print('-=' * 25)
print('Original list: {}, sum of numbers: {}' .format(list, sum(list)))
print('Sorted list: {}' .format(sorted(list)))
print('Even numbers: {}, sum of even numbers: {}' .format(even, sum(even)))
print('Odd numbers: {}, sum of odd numbers: {}' .format(odd, sum(odd)))
print('Prime numbers: {}, sum of prime numbers {}' .format(prime, sum(prime)))
print('-=' * 25)
