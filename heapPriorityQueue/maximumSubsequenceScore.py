import heapq
def maxScore(nums1, nums2, k):
    n = len(nums1)
    # pair the values of nums1 and nums2 together
    # sort based on nums2(x[1]) in descending order (-)
    pairs = sorted(zip(nums1, nums2), key = lambda x: -x[1])

    max_score = 0
    current_sum = 0
    min_heap = []

    for i in range(n):
        num1, num2 = pairs[i]
        heapq.heappush(min_heap, num1)
        current_sum += num1

        if len(min_heap) > k:
            current_sum -= heapq.heappop(min_heap)

        if len(min_heap) == k:
            max_score = max(max_score, current_sum * num2)
    return max_score

nums1 = [1,3,3,2] # sum of selected k elements
nums2 = [2,1,3,4] # min of selected k elements
k = 3
result = maxScore(nums1, nums2, k)
print(result)