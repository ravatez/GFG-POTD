from collections import Counter
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        
    
        # Calculate frequency of each character
        frequency = Counter(s)
        
        x = 0
        y = 0
        
        for char, freq in frequency.items():
            position = ord(char) - ord('a') + 1  # Position in the alphabet (1-based index)
            
            if position % 2 == 0:  # Even position
                if freq % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position
                if freq % 2 == 0:  # Odd frequency
                    continue
                else:
                    y += 1
        
        # Sum x and y
        total = x + y
        
        # Determine if total is even or odd
        if total % 2 == 0:
            return "EVEN"
        else:
            return "ODD"    



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends