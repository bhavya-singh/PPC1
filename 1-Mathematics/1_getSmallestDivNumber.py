#Author	:	Bhavya Singh
#Date	:	17-May-2020
#Name	:	Smallest divisible number

#PROBLEM: Given a number n the task is to complete the function which returns an integer denoting the smallest number evenly divisible by each number from 1 to n.

#Input:
The first line of input contains an integer T denoting the no of test cases then T test cases follow. Each line contains an integer N.

#Output:
For each test case output will be in new line denoting the smallest number evenly divisible by each number from 1 to n.

#Constraints:
1<=T<=50
1<=n<=25


#Example(To be used only for expected output):
Input:
2
3 
6
Output:
6
60

#CODE

def gcd(a, b):

    if b == 0:

        return a

    else:

        return gcd(b, a%b)



def getSmallestDivNum(n):

    lcm = 1
    
    for i in range(1, n + 1):

	        lcm = (lcm * i)//gcd(lcm, i)

    return lcm
