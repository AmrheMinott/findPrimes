# findPrimes

This application was done to test my understanding of the following
  Run time complexity -> the aim is to find primes number in a given range example 2-50. However there are three method used to find these prime done in this python program.

    Method 1: We go through each number of the range and compare that number to every number previously seen
      Analysis: this function using this method runs in O(n^2) time complexity

    Method 2: Create a simulated storage bank (primesArray) that holds the all the newly found prime numbers. For comparison instead of going over every number from the beginning we go over every number in the prime number memory bank
      Analysis: by implementing this approach we are no longer running at O(n^2) instead we are running at O(n*m) where n is the elements in the range given to find the prime numbers and m is the number of prime numbers we have found in (primesArray)

    Method 3: This method is very similar to method 2 above
      Analysis: however if we know that one of our primes from the primesArray can divide evenly into a number from the range then there is no need to continue thus we break from the loop and move on to the next number in the range.



  User input/output   -> handling values from the user


  Most importantly this was just for fun
    Honestly I was just curious  to see how this code would look in the end and I had fun thinking on it... until my next coding project
