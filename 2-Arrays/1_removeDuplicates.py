#Author	:	Bhavya Singh
#Date	:	22-May-2020
#Name	:	Remove Duplicate Elements from a sorted array

#PROBLEM:

Given a sorted array A of size N. The function remove_duplicate takes two arguments . The first argument is the sorted array A[ ] and the second argument is 'N' the size of the array and returns the size of the new converted array A[ ] with no duplicate element.

Input Format:
The first line of input contains T denoting the no of test cases . Then T test cases follow . The first line of each test case contains an Integer N and the next line contains N space separated values of the array A[ ] .

Output Format:
For each test case output will be the transformed array with no duplicates.

Your Task:
Your task to complete the function remove_duplicate which removes the duplicate  elements from the array .

Constraints:
1 <= T <= 100
1 <= N <= 104
1 <= A[ ] <= 106

Example:
Input  (To be used only for expected output) :
2
5
2 2 2 2 2 
3
1 2 2
Output
2
1 2



#CODE

def remove_duplicate(n, arr):
    list_set = set()
    for index in range(n):
        list_set.add(arr[index])
    arr.clear()
    for element in list_set:
        arr.append(element)
    arr.sort()
    return len(list_set)

