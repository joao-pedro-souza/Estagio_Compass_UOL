for n in range(1, 101):
    divisivel = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            divisivel += 1
    if divisivel == 2:
        print(n)