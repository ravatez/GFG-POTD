class Solution:
    def mergeArrays(self, a, b):
        # code here
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2  
        def next_gap(gap):
            if gap <= 1:
                return 0
            return (gap + 1) // 2
        
        while gap > 0:
            i, j = 0, gap
            while j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                i += 1
                j += 1
            j -= n 
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
            i = 0
            while j < m:
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
                i += 1
                j += 1
            gap = next_gap(gap)

#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends