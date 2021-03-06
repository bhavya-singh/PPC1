#Author	:	Bhavya Singh
#Date	:	19-May-2020
#Name	:	Exactly 3 Divisors

#THEORY:

Not many numbers have exactly 3 divisors.
You may try writing some numbers (from 1 to 25) with pen and paper and may notice a pattern.
After having a close look on examples mentioned above, you have noticed that all the required numbers are perfect squares and that too are only of primes numbers. The logic behind this is, such numbers can have only three numbers as their divisor and also that include 1 and that number itself resulting into just a single divisor other than number, so we can easily conclude that required are those numbers which are squares of prime numbers so that they can have only three divisors (1, number itself and sqrt(number)). So all primes i, such that i*i is less than equal to N are three-prime numbers.
Note: We can generate all primes within a set using any sieve method efficiently and then we should all primes i, suct that i*i <=N.

#PROBLEM: 

Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

Input:
The first line contains integer T, denoting number of test cases. Then T test cases follow. The only line of each test case contains an integer N.

Output:
For each testcase, in a new line, print the answer of each test case.

Your Task:
This is a function problem. You only need to complete the function exactly3Divisors() that takes N as parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

Constraints :
1 <= T <= 105
1 <= N <= 109

Example:
Input :
3
6
10
30
Output :
1
2
3

Explanation:
Testcase 1: There is only one number 4 which has exactly three divisors 1, 2 and 4.
Testcase 2: 4 and 9 are the only two numbers less than or equal to 10 that have exactly three divisors.
Testcase 3: 4, 9, 25 are the only numbers less than or equal to 30 that have exactly three divisors.

#CODE

def exactly3Divisors(N):

    primes = [True]*(N+1)

    primes[0] = primes[1] = False

    i = 1

    while i*i <= N:

        if primes[i]:

            for j in range(i*2, N+1, i):

                primes[j] = False

        i += 1

    count = 0

    i = 0

    while( i*i <= N):

        if primes[i]:

            count += 1

        i += 1

    return(count)