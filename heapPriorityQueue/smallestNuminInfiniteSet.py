import heapq

class SmallestInfiniteSet:
        def __init__(self):
                self.current = 1 # maintain an integer (current) to represent the smalles number that has not yet been poped.
                self.added_back = [] # use a min-heap (added_back) to track any numbers added back
        
        def popSmallest(self) -> int:
            if self.added_back:
                # if there are elements in the heap, pop the smallest
                smallest =  heapq.heappop(self.added_back)
                return smallest
            else:
                # if no elements in the heap, return the current smallest
                smallest = self.current
                self.current += 1
                return smallest
            
        def addBack(self, num: int) -> None:
            # add the number back if it's smaller than the current and not in the heap.
            if num < self.current and num not in self.added_back:
                heapq.heappush(self.added_back, num)


smallestInfiniteSet = SmallestInfiniteSet()
smallestInfiniteSet.addBack(2)       # No effect as 2 is still in the set.
print(smallestInfiniteSet.popSmallest())  # Returns 1.
print(smallestInfiniteSet.popSmallest())  # Returns 2.
print(smallestInfiniteSet.popSmallest())  # Returns 3.
smallestInfiniteSet.addBack(1)       # Adds 1 back to the set.
smallestInfiniteSet.addBack(2)
smallestInfiniteSet.addBack(2)
print(smallestInfiniteSet.popSmallest())  # Returns 1.
print(smallestInfiniteSet.popSmallest())  # Returns 2.
print(smallestInfiniteSet.popSmallest())  # Returns 4.
print(smallestInfiniteSet.popSmallest())  # Returns 5.                       
