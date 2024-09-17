#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    #code here
	    n=len(arr)
	    if arr[0]==0:
	        return -1
	    if n==1:
	        return 0
	    mR=sE=arr[0] #i=maximum reach j= end of the range for the current jump
	    jump=1
	    for i in range (1,n):
	        if i==n-1:
	            return jump
	        mR=max(mR,i+arr[i]) #furtest point of reach
	        if i==sE:
	            jump+=1
	            sE=mR
    	        if sE>=n-1:
    	            return jump #already reached last element before completing the steps
    	    if mR<=i:
    	        return -1
    	            
	    return -1
	        
	            
	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends