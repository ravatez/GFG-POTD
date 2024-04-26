#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
        # Define directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize current position and direction
        row, col = 0, 0
        direction_index = 0  # Start moving right
        
        while True:
            # Check if current position is outside the matrix
            if row < 0 or row >= n or col < 0 or col >= m:
                return [row - directions[direction_index][0], col - directions[direction_index][1]]
            
            # Check if current cell is 1, then change direction and update cell value
            if matrix[row][col] == 1:
                direction_index = (direction_index + 1) % 4  # Change direction
                matrix[row][col] = 0  # Change cell value
                
            # Move in the current direction
            row += directions[direction_index][0]
            col += directions[direction_index][1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends