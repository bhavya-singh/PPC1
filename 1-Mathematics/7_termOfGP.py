#Author	:	Bhavya Singh
#Date	:	17-May-2020
#Name	:	GP Term

#THEORY:

A GP is represented as - a, a*r, a*r^2, a*r^3,...
Common ratio - a*r/a or a*r^2/a*r,...
nth term of a GP - a*r^(n-1)

#PROBLEM:

GP Term
Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case in its first line contains two positive integer A and B (First 2 terms of GP). In the second line of every test case it contains of an integer N.

Output:
In each seperate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

Your Task:
This is a function problem. You need to complete the function termOfGP() that takes A and B as parameter and returns Nth term of GP. The return value should be double that would be automatically converted to floor by the driver code.

Constraints:
1 <= T <= 100
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Example:
Input:
2
2 3
1
1 2
2
Output:
2
2

Explanation:
Testcase 1: Since we need to find the 1st element, we know it is 2 as first element is 2 and second is 3.
Testcase 2: The second term of series whose common ratio is 2 will be 2.



#CODE

def termOfGP(A,B,N):

    if N==1:

        return A

    elif N==2:

        return B

    else:

        return float(A*((B/A)**(N-1)))