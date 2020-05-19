#Author	:	Bhavya Singh
#Date	:	17-May-2020
#Name	:	Digits in Factorial

#THEORY:

We know,
log(a*b) = log(a) + log(b)

Therefore
log( n! ) = log(1*2*3....... * n) 
          = log(1) + log(2) + ........ +log(n)

Now, observe that the floor value of log base 
10 increased by 1, of any number, gives the
number of digits present in that number.

Hence, output would be : floor(log(n!)) + 1.

#PROBLEM:

Given an integer N. The task is to find the number of digits that appear in its factorial, where factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.

Input:
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer N.

Output:
Corresponding to each test case, in a new line, print the number of digits that appear in its factorial.

Your Task:
This is a function problem. You only need to complete the function digitsInFactorial() that takes N as parameter and returns number of digits in factorial of N.

Constraints:
1 = T = 100
1 = N = 104

Example:
Input:
2
5
120
Output:
3
199

Explanation:
Testcase 1: Factorial of 5 is 120. Number of digits in 120 is 3 (1, 2, and 0).
Testcase 2: Number of digits in 120! is 199.



#CODE

def digitsInFactorial(N):

    if N < 0:

        return 0

    elif N <= 1:

        return 1

    else:

        digits = 0

        for i in range(2, N+1):

            digits += math.log10(i)

        return math.floor(digits)+1