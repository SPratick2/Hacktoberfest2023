n=int(input())
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
fibonacci_series = [fib(i) for i in range(n)]
print(fibonacci_series)
#prints the series upto n terms
