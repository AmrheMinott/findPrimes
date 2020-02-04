# import module
import time


'''
    this program function in O(n^2) where each loop of the range of number given by the user
    we go through from the begining comparing each time
'''
def findPrimesTheLongWay(ranges, start, primesArray):
    isPrime = "is"
    for i in range(start, ranges):
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
def findPrimesTheSemiLongWay(ranges, start, primesArray):
    isPrime = "is"
    for i in range(start, ranges):
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
def findPrimesTheOptimisedWay(ranges, start, primesArray):
    isPrime = "is"
    # highly optimisied using the break statement
    for i in range(start, ranges):
        for y in primesArray: # we are looping through the members of the primes array
            if (i%y == 0): # not a prime
                isPrime = "not"
                break # we exit early once we have found our case not a prime

        # if string is NOT equal to "not" then we can append the digit i to the primes collection
        if isPrime != "not":
            primesArray.append(i)
        isPrime = "is"


# this function prints our arrays in a neat and tidy columns
def printPrimes(primesArray, func):
    if func == 0:
        print(f"\n\nPrimes found by the long method ")
    elif func == 1:
        print(f"\n\nPrimes found by the SEMI-LONG method ")
    else:
        print(f"\n\nPrimes found by the OPTIMIZED method")


    columns = 5; # this variable is the number of columns I wish to see for the data
    rows = int((len(primesArray)/2))+1 # calculated using the length of the array divided by 2 plus 1
    printer = ""
    for i in range(rows):
        for x in range(columns):
            if len(primesArray) == 0:
                break
            printer += "\t" + str(primesArray.pop(0)) + "\t"
    print(f"{printer}")
    printer = ""

# this function determines the time of the function we are running
def timeMe(functionName , func, ranger, START_VALUE, primes):
    start = time.time()
    if func == 0:
        findPrimesTheLongWay(ranger, START_VALUE, primes)
    elif func == 1:
        findPrimesTheSemiLongWay(ranger, START_VALUE, primes)
    else:
        findPrimesTheOptimisedWay(ranger, START_VALUE, primes)
    end = time.time()

    # prints the name of the function plus the time it took to complete execting as well as the number of loops that were done
    print(f"{functionName} took {end - start} to find primes in the range {range}")

def main():

    START_VALUE = 2 # where we start count in our range
    WAIT_TIME = 5 # total wait time on display
    SLEEP = 1; # the wait periods inbetween the function calls
    primes = [] # this array holds our value for the primes number we have found


    range = input("Insert value for number of range\n") # use inputs value for the range they wish to find primes in
    while not(range.isdigit()): # error handling is done here where if the user inputs a string the loop continues until an int is inputted
        range = input("Insert an integer for number of range\n")
    range = int(range) # convert the string version of an int to an actual useable int


    print(f"We are going to find the prime numbers between 1 and {range} the LONG way")
    input("Press enter to execute \"findPrimesTheLongWay\"")

    timeMe("findPrimesTheLongWay" , 0 , range, START_VALUE, primes)
    printPrimes(primes , 0)


    primes.clear()
    print("Array cleared...ready for SEMI-LONG")
    input("Press enter to execute \"findPrimesTheSemiLongWay\"")


    timeMe("findPrimesTheSemiLongWay" , 1 , range, START_VALUE, primes)
    printPrimes(primes , 1)


    primes.clear()
    print("Array cleared...ready for OPTIMIZED way")
    input("Press enter to execute \"findPrimesTheOptimisedWay\"")

    timeMe("findPrimesTheOptimisedWay" , 2 , range, START_VALUE, primes)
    printPrimes(primes , 2)

# we are calling main to run the function we just created
main()




# end of python program
