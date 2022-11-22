def factorial_calcuclator(x):
    if x == 1:
        return 1
    else:
        return x * factorial_calcuclator(x - 1)


namba = int(input("Enter The Number to check the factorial\n"))

print("The factorial of", namba, "is", factorial_calcuclator(namba))
