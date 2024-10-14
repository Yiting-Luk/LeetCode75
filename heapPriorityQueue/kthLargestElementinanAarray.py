import heapq
def findKthLargest(nums, k):
    heap = nums[:k] # create a min-heap with the first k elements
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num) 
    
    return heap[0] 

nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(findKthLargest(nums1, k1))  # Output: 5