import math
cmd=int(input("input problem number: "))
if cmd==1:
    sum=i=0
    n=int(input("Give the value of n: "))
    while i <= n:
        sum=sum+i
        i=i+2
    print("The sum is even numbers up to ",n," is ",sum)
elif cmd==2:
    prime=True
    n=int(input("Give the value of n: "))
    for i in range(2,n-1):
        if n%i==0:
            prime=False
    print("n is a prime number is",prime)
else:
    print("yep, thats an invalid problem number :V")