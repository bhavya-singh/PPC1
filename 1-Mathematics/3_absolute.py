#Author	:	Bhavya Singh
#Date	:	17-May-2020
#Name	:	Absolute Value

#PROBLEM:

You are given an interger I. You need to print the absolute value of the interger I.

Input:
The first line of input contains T, denoting number of testcases. Each testcase contains single integer I which may be positive or negative.

Output:
For each testcase, in a new line, output the absolute value.

Your Task:
This is function problem. You only need to complete the function absolute that takes integer I as parameter and returns the absolute value of I. All other things are taken care of by the driver code.

Constraints:
1 <= T <= 100
-106 <= I <= 106

Example:
Input:
2
-32
45
Output:
32
45

Explanation:
Testcase 1: Since -32 is negative, we prints its positive equavalent, i.e., 32
Testcase 1: Since 45 is positive, we prints its value as it is, i.e., 45


#CODE

def absolute(I):

    return abs(I)
