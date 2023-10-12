# Function to generate a Fibonacci sequence
def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Check if the input is valid
    if n <= 0:
        return []
    elif n == 1:
        return [a]
    elif n == 2:
        return [a, b]
    
    # Generate the Fibonacci sequence
    fibonacci_sequence = [a, b]
    for _ in range(2, n):
        a, b = b, a + b
        fibonacci_sequence.append(b)
    
    return fibonacci_sequence

# Number of Fibonacci numbers to generate
n = 10

# Generate and print the Fibonacci sequence
fib_sequence = generate_fibonacci(n)
print(f"Fibonacci sequence of {n} numbers: {fib_sequence}")
