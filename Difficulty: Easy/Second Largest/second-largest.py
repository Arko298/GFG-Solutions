#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        arr.sort(reverse=True)
        n = len(arr)
        #we can say that the 1st element is the largest so we can start the loop from the second element. Thus we can find out weather the 2nd element is largest or not
        for i in range(1,n):
            if arr[i]!=arr[0]:#this step basically sees that the 2nd element is same as 1st or not...if yes return -1 as example states [10,10] should give -1
                return arr[i]
        return -1
            
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends