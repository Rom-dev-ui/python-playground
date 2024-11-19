# main.py - A playground for experimenting with Python code

def hello_world():
    """Simple function to print 'Hello, World!'"""
    print("Hello, World!")

def fibonacci(n):
    """Generate the first n numbers of the Fibonacci sequence"""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def prime_numbers(limit):
    """Return a list of prime numbers up to a given limit"""
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def main():
    """Main function to test different functionalities"""
    print("Python Playground - Testing various functions")
    
    # Test hello_world function
    hello_world()

    # Test Fibonacci sequence function
    n = 10
    print(f"First {n} numbers of the Fibonacci sequence: {fibonacci(n)}")

    # Test prime number function
    limit = 30
    print(f"Prime numbers up to {limit}: {prime_numbers(limit)}")

if __name__ == "__main__":
    main()

