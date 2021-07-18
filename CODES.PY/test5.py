def powerof(n):
    if n ==0:
        return 1
    else:
        power=powerof(n-1)
        return power *2


