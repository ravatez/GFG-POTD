#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        total_sum = 0
        
        for bit_pos in range(32):
            count = 0
            for num in arr:
                if num & (1 << bit_pos):
                    count += 1
            total_sum += (count * (count - 1) // 2) * (1 << bit_pos)
        
        return total_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends