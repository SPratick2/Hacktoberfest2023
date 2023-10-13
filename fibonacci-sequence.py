# Program to display the Fibonacci sequence up to n-th term

a=0
b=1
# for user input
num =int(input("Enter a number to add fibonacci sequence:"))
if num ==1:
    print(a)
else:
    print(a)
    print(b)
for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c)