

def findPrimesTheLongWay(LOOPS, start, primesArray):
    isPrime = "is"
    for i in range(start, LOOPS):
        for y in range(start, i):
            if (i%y == 0): # not a prime
                isPrime = "not"
        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"

def findPrimesTheSemiLongWay(LOOPS, start, primesArray):
    isPrime = "is"
    for i in range(start, LOOPS):
        for y in primesArray:
            if (i%y == 0): # not a prime
                isPrime = "not"

        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"

def findPrimesTheOptimisedWay(LOOPS, start, primesArray):
    isPrime = "is"
    # highly optimisied using the break statement
    for i in range(start, LOOPS):
        for y in primesArray: # we are looping through the members of the primes array
            if (i%y == 0): # not a prime
                isPrime = "not"
                break # we exit early once we have found our case not a prime

        # if string is NOT equal to "not" then we can append the digit i to the primes collection
        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"


def main():

    STRAT_VALUE = 2
    LOOPS = int(input("Insert value for number of LOOPS\n"))
    primes = []

    print(f"We are going to find the prime numbers between 1 and {LOOPS} the LONG way")
    input("Press enter to execute \"findPrimesTheLongWay\"")
    findPrimesTheLongWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the long method {primes}")


    print("Clearing array ...\n\n\n");


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the SEMI-LONG way")
    input("Press enter to execute \"findPrimesTheSemiLongWay\"")
    findPrimesTheSemiLongWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the SEMI-LONG method {primes}")


    print("Clearing array ...\n\n\n");


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the OPTIMIZED way")
    input("Press enter to execute \"findPrimesTheOptimisedWay\"")
    findPrimesTheOptimisedWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the OPTIMIZED method {primes}\n\n")

main()
