n=int(input())
is_armstrong = lambda n: n == sum(int(digit) ** len(str(n)) for digit in str(n))
print(is_armstrong(n))
