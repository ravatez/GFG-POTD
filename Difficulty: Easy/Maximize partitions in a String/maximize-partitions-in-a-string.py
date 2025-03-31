class Solution:
    def maxPartitions(self , s):
        # code here
        # code here
        
        intervals = {c:i for i,c in enumerate(s)}
        # print(intervals)
        
        f_max=-1
        cnt=0
        
        for i,c in enumerate(s):
            
            f_max=max(f_max,intervals[c])
            
            if f_max==i:
                cnt+=1
                
        return cnt

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends