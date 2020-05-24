#Author	:	Bhavya Singh
#Date	:	22-May-2020
#Name	:	Find Transition Point

#PROBLEM:

You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. Transition point is a point where "0" ends and "1" begins (0 based indexing).
Note that, if there is no "1" exists, print -1.

Input:

The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and second line will be the elements of the array.

Output:

Your function should return transition point.

Your Task:
The task is to complete the function transitionPoint() that takes array and N as input and returns the value of the position where "0" ends and "1" begins.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:

1 = T = 100
1 = N = 500000
0 = C[i] = 1
Example:

Input
2
5
0 0 0 1 1
4
0 0 0 0

Output
3
-1

Explanation:
Testcase 1: position 3 is 0 and next one is 1, so answer is 3.
Testcase 2: Since, there is no "1", so the answer is -1.


#CODE

import collections

def transitionPoint(arr, n):

    c = collections.Counter(arr)

    if(c[1]==0):

        return -1

    else:

        return c[0]

#Without 'import'

def transitionPoint(arr, n):

    cnt_0 = 0

    cnt_1 = 0

    for i in arr:

        if i==0:

            cnt_0 +=1

        elif i==1:

            cnt_1 +=1

    if(cnt_1==0):

        return -1

    else:

        return cnt_0