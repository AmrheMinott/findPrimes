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
    columns = 5;
    rows = int((len(primesArray)/2))+1
    printer = ""
    for i in range(rows):
        for x in range(columns):
            if len(primesArray) == 0:
                break
            printer += "\t" + str(primesArray.pop(0)) + "\t"
    print(f"{printer}")
    printer = ""

def timeMe(functionName , func, LOOPS, START_VALUE, primes):
    start = time.time()
    if func == 0:
        findPrimesTheLongWay(LOOPS, START_VALUE, primes)
    elif func == 1:
        findPrimesTheSemiLongWay(LOOPS, START_VALUE, primes)
    else:
        findPrimesTheOptimisedWay(LOOPS, START_VALUE, primes)
    end = time.time()

    print(f"{functionName} took {end - start} to find primes in the range {LOOPS}")

def main():

    START_VALUE = 2 # where we start count in our range
    WAIT_TIME = 5 # total wait time on display
    SLEEP = 1; # the wait periods inbetween the function calls

    LOOPS = input("Insert value for number of LOOPS\n") # use inputs value for the range they wish to find primes in
    while not(LOOPS.isdigit()): # error handling is done here where if the user inputs a string the loop continues until an int is inputted
        LOOPS = input("Insert an integer for number of LOOPS\n")
    LOOPS = int(LOOPS) # convert the string version of an int to an actual useable int
    primes = [] # this array holds our value for the primes number we have found


    print(f"We are going to find the prime numbers between 1 and {LOOPS} the LONG way")
    input("Press enter to execute \"findPrimesTheLongWay\"")

    timeMe("findPrimesTheLongWay" , 0 , LOOPS, START_VALUE, primes)
    print(f"\n\nPrimes found by the long method ")
    printPrimes(primes)


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the SEMI-LONG way")
    input("Press enter to execute \"findPrimesTheSemiLongWay\"")


    timeMe("findPrimesTheSemiLongWay" , 1 , LOOPS, START_VALUE, primes)
    print(f"\n\nPrimes found by the SEMI-LONG method ")
    printPrimes(primes)


    primes.clear()
    print(f"We are going to find the prime numbers between 1 and {LOOPS} the OPTIMIZED way")
    input("Press enter to execute \"findPrimesTheOptimisedWay\"")

    timeMe("findPrimesTheOptimisedWay" , 2 , LOOPS, START_VALUE, primes)
    print(f"\n\nPrimes found by the OPTIMIZED method \n\n")
    printPrimes(primes)

# we are calling main to run the function we just created
main()
