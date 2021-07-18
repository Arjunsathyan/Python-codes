'''n=int(input('Enter the number'))
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1

    j=1
    while j<=2*i-1:
        print('*',end="")
        j=j+1

    print()
    i=i+1'''
    n=int(input('Enter the number'))
    m=(n+1)/2
    i=1
    while i<=n:
        if (i > m):
            s=n-1
            sr=2*(m-1)+1

        else:
            s=
