# User function Template for python3

class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        # Your code here
        n=len(arr)
        left=[0]*n
        right=[-1]*n
        if n==1:
            return 1
        left[0]=0
        right[-1]=0
        for i in range(1,n):
            left[i]=arr[i-1]+left[i-1]
        for i in range (n-2,-1,-1):
            right[i]=arr[i+1]+right[i+1]
        for i in range (n):
            if left[i]-right[i]==0:
                return i+1
        return -1
        
        
       
            
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.equilibriumPoint(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends