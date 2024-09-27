def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2))

n_terms = int(input("Please enter fibonacci terms : "))

if n_terms < 0:
    print("Invalid Input !")
else:
    print("Fibonacci Series :")
for i in range(n_terms):
    print(recursive_fibonacci(i))