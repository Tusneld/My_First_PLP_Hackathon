# Python program: Generate Fibonacci sequence up to a specified term
# Author: Tusnelde L.S Endjala
# This program generates the Fibonacci sequence up to a specified term provided by the user.
# It uses memoization to optimize the calculation of Fibonacci sequence and prints the generated sequence.

# Function to generate Fibonacci sequence using memoization
def generate_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2: 
        return [0, 1]
    else:
        # Recursive call with memoization
        fib_sequence = generate_fibonacci(n - 1, memo)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        memo[n] = fib_sequence
        return fib_sequence

# Asking user for input
n = int(input("Enter the value of n: "))

# Generating Fibonacci sequence and printing it
fibonacci_sequence = generate_fibonacci(n)
print("Generated Fibonacci sequence:", fibonacci_sequence)
