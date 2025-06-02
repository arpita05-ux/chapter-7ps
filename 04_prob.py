n = int(input("Enter a number: "))

for i in range(2,n):   # When checking divisibility, start from 2.Because 1 divides everything, and gives wrong result for primes 
    if(n%i) == 0:
        print("Number is not prime")
        break
    else:
        print("It is a prime number")