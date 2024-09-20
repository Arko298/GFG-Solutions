#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        n=len(height)
        count=1
        
        if n==0:
            return -1
        if n==1:
            return count
        a=height[0]
        for i in range(1,n):
            if a<height[i]:
                count+=1
                a=height[i]
                
                
               
            
        return count
 
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends