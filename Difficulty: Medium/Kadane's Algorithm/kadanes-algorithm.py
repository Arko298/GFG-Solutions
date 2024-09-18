#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        # summ=0
        # max_sum=float('-inf')
        # for i in arr:
        #     summ+=summ+i
        #     max_sum=max(max_sum,summ)
        #     if summ<0:
        #         summ=0
            
        # return max_sum
        summ=arr[0]
        max_sum=arr[0]
        for i in range (1,len(arr)):
            summ=max(arr[i],summ+arr[i])
            max_sum=max(summ,max_sum)
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends