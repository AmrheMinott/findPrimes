# import module
import time


'''
    this program function in O(n^2) where each loop of the range of number given by the user
    we go through from the begining comparing each time
'''
def findPrimesTheLongWay(LOOPS, start, primesArray):
    isPrime = "is"
    for i in range(start, LOOPS):
        for y in range(start, i):
            if (i%y == 0): # not a prime
                isPrime = "not"
        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"
'''
    this function is slighly faster in performance as we are adding the newly found prime numbers
    to a simulated memory (the array) where each new number is compared to the number int he array -> primesArray
'''
def findPrimesTheSemiLongWay(LOOPS, start, primesArray):
    isPrime = "is"
    for i in range(start, LOOPS):
        for y in primesArray:
            if (i%y == 0): # not a prime
                isPrime = "not"

        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"

'''
    very very similar to the function above except for one line of code. The break statement that one line allows us
    to say "you are not a prime so there is no need t look any futher"
'''
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

def printPrimes(primesArray):

    printer = ""
    count = 0
    for x in primesArray:
        printer += "\t" + str(x) + "\t"
        count += 1
        if count == 5:
            count = 0
            print(f"{printer}")
            printer = ""


def main():

    STRAT_VALUE = 2 # where we start count in our range
    WAIT_TIME = 5 # total wait time on display
    SLEEP = 1; # the wait periods inbetween the function calls
    LOOPS = int(input("Insert value for number of LOOPS\n")) # use inputs value for the range they wish to find primes in
    primes = []

    print(f"We are going to find the prime numbers between 1 and {LOOPS} the LONG way")
    input("Press enter to execute \"findPrimesTheLongWay\"")
    findPrimesTheLongWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the long method ")

    printPrimes(primes)



    print(f"\n\nWait {WAIT_TIME} seconds we are clearing array from findPrimesTheLongWay for next test ...");
    time.sleep(SLEEP);
    print("The next function to test is findPrimesTheSemiLongWay\n\n");
    time.sleep(SLEEP);


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the SEMI-LONG way")
    input("Press enter to execute \"findPrimesTheSemiLongWay\"")
    findPrimesTheSemiLongWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the SEMI-LONG method ")
    printPrimes(primes)


    print(f"\n\nWait {WAIT_TIME} seconds we are clearing array from findPrimesTheSemiLongWay for next test ...");
    time.sleep(SLEEP);
    print("The next function to test is findPrimesTheOptimisedWay\n\n");
    time.sleep(SLEEP);


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the OPTIMIZED way")
    input("Press enter to execute \"findPrimesTheOptimisedWay\"")
    findPrimesTheOptimisedWay(LOOPS, STRAT_VALUE, primes)
    print(f"\n\nPrimes found by the OPTIMIZED method \n\n")
    printPrimes(primes)

# we are calling main to run the function we just created
main()
