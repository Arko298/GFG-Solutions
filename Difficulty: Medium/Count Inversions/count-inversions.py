class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def __init__(self):
        self.count = 0  # Initialize inversion count
    
    def count_and_merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid 
        L = [0] * n1
        R = [0] * n2
        
        for i in range(n1):
            L[i] = arr[left + i]
        for i in range(n2):
            R[i] = arr[mid + 1 + i]
        
        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                self.count += (n1 - i)  # Count inversions
            k += 1
        
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def count_inversions(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.count_inversions(arr, left, mid)
            self.count_inversions(arr, mid + 1, right)
            self.count_and_merge(arr, left, mid, right)
                
    def inversionCount(self, arr):
        self.count = 0  # Reset count for new input
        self.count_inversions(arr, 0, len(arr) - 1)
        return self.count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))

# } Driver Code Ends