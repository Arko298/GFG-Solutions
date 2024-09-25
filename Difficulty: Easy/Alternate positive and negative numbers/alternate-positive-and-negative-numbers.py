#User function Template for python3

class Solution:
    def rearrange(self,arr):
        nl=len(arr)
        pos=[]
        neg=[]
        for i in range(nl):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        p=0
        n=0
        i=0
        while p<len(pos) and n<len(neg):
            if i%2==0:
                arr[i]=pos[p]
                p+=1
            else:
                arr[i]=neg[n]
                n+=1
            i+=1
        while p<len(pos):
            arr[i]=pos[p]
            i+=1
            p+=1
        while n<len(neg):
            arr[i]=neg[n]
            i+=1
            n+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends