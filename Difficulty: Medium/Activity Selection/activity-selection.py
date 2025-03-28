class Solution:
    def activitySelection(self, start, finish):
        #code here
        point=0
        last = -1
        for a,b in sorted(zip(start,finish)):
            if a>last:
                point+=1
                last = b 
            else:
                last = min(b,last)
        return point

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends