"""
*********************** Complexity Analysis ***********************

Complexity Analysis: a method of determining the efficiency of algorithms
                     that allows you to rate them independently of platform-
                     dependent timings or impractical instruction counts.

Order of complexity: the difference in performance of your algorithms

linear: grows in direct proportion to the size of the problem.

quadratic: grows as a function of the square of the problem size

polynomial time algorithm: grows at a rate of n raised to k

exponential: a growth rate of x raised to n. these are impractical to run
             with large problem sizes

logarithmic: proportional to the log base 2 of the problem size

*********************** Big-O Notation ***********************

dominant: The term with an amount of work in an algorithm that becomes so large that you
          can ignore the amount of work represented by the other terms
          (1/2)n^2-(1/2)n
          n^2 is dominant here

          Represented with Big-O notation
          O(n^2)
    practice:  1) a = O(2^n), b = O(2^n), c = O(n^3)
               2) B does more work
               3) 4 items in collection

Constant O(1)
    - Time taken is independent of the amount of data
    - Stack push, pop and peek; Queue, dequeue and enqueue; Insert a node
        into a linked list

Linear O(n)
    - Time taken is directly proportional to the amount of data
    - Linear search; Count items in a list; Compare a pair of strings

Quadratic O(n^2)
    - Time taken is proportional to the amount of data squared, twice as much data
        data takes 4 times as long to process, poor scalability
    - Bubble sort; Selection sort; Insertion sort; Traverse a 2D array

Polynomial O(n^k)
    - Time taken is proportional to the amount of data raised to the power of
        a constant

Logarithmic O(log n)
    - Time taken is proportional to the logarithm of the amount of data,
        good scalability
    - Binary search a sorted list; Search a binary tree; Divide and conquer
      algorithm approaches

Linerarithmic O(n log n)
    - Time taken is proportional to the logarithm of the amount of data,
        multiplied by the amount of data

Exponential O(k^n)
    - Time taken is proportional to a constant raised to the power of the amount of data,
        very poor scalability almost immediately.
    - If constant k is 10, then one extra item of data will slow it down by ten times

Logarithm - The inverse of exponentiation

    - Generally
        x^z = y    log base x of y = z

        2^0 = 1    log base 2 of 1 = 0
        2^1 = 2    log base 2 of 2 = 1
        2^2 = 4    log base 2 of 4 = 2
        2^3 = 8    log base 2 of 8 = 3
        2^4 = 16   log base 2 of 16 = 4

        10^4 = 10000  log base 10 of 10000 = 4

        note that each number we're calculating the log of is twice as much
        the previous number but each log is only 1 bigger than the previous value

"""