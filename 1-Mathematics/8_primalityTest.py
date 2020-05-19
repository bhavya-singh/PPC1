#Author	:	Bhavya Singh
#Date	:	17-May-2020
#Name	:	Primality Test

#PROBLEM:

Primality Test
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case should contain a positive integer N.

Output:
For each testcase, in a new line, print "Yes" if it is a prime number else print "No".

Your Task:
This is a function problem. You just need to complete the function isPrime that takes N as parameter and returns True if N is prime else returns false. The printing is done automatically by the driver code.

Constraints:
1 <= T <= 100
1 <= N <= 103

Example:
Input:
2
5
4
Output:
Yes
No

Explanation:
Testcase 1: 5 is the prime number as it is divisible only by 1 and 5.
Testcase 2: 4 is not a prime number as it is divisible by 1 2 and 4.


#CODE

def isPrime(N):

    if (N==1): #1 is not prime so return false

        return True

    for i in range(2,1+int(math.sqrt(N))): #We check from 2 from sqrt(N) as divisors, if any, would exist till sqrt(N)
        
	if N%i==0: #If any i divides the number this means the number is not prime

            return False

    return True #return true in either cases