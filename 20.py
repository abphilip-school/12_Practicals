def cube(n):
    return n**3

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

def powersOfTwo(n):
    for i in range(n):
        yield 2**i

def menu()
    a = int(raw_input("1. Cube\n2. Fibonacci\n3. Powers of 2\n--> "))
    n = int(raw_input("Enter the number: "))
    if a == 1:
        c = cube(n)
        print c
    elif a == 2:
        fib(n)
    elif a == 3:
        powersOfTwo(n)
    else:
        print "Try Again..."
        menu()

menu()
