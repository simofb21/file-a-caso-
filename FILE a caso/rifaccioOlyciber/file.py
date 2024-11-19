def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(20)
print("Numero di chiamate di f per calcolare f(20):", result)
