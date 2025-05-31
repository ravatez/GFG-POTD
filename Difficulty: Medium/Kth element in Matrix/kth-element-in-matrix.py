from heapq import *
class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        max_heap = []
        n = len(matrix)
        new_matrix = []
        for i in range(n):
            new_matrix.extend(matrix[i])
        for i in range(k):
            heappush(max_heap, -1*new_matrix[i])
        for i in range(k,n*n):
            if -1*new_matrix[i]>max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -1*new_matrix[i])
        return -1*max_heap[0]