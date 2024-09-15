#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        
        count={}
        n=len(arr)/2
        for num in arr:
            count[num]=count.get(num,0)+1
            if count[num]>n:
                
                return num
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends