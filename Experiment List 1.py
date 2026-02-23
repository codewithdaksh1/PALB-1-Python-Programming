# 1. You are given an array of integers arr[]. You have to reverse the given array.
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        return arr

# 2. Given an array arr[]. Your task is to find the minimum and maximum elements in the array.
class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]

        for num in arr:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num

        return [minimum, maximum]


# 3. Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
class Solution:
    def kthSmallest(self, arr, k):
        arr = sorted(arr)
        return arr[k-1]


# 4. You are given two arrays a[] and b[], return the Union of both the arrays in any order.
class Solution:
    def findUnion(self, a, b):
        s = set()

        for num in a:
            s.add(num)

        for num in b:
            s.add(num)

        return list(s)


# 5. Given an array arr[]. The task is to find the largest element and return it.
class Solution:
    def largest(self, arr):
        largest = arr[0]

        for num in arr:
            if num > largest:
                largest = num

        return largest


# 6. Given an array arr, rotate the array by one position in clockwise direction.
class Solution:
    def rotate(self, arr):
        last = arr[len(arr)-1]

        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]

        arr[0] = last
        return arr


# 7. You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
class Solution:
    def maxSubarraySum(self, arr):
        max_sum = arr[0]
        current_sum = arr[0]

        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


# 8. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where 
#    it would be if it were inserted in order.
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# 9. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number -> index

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


# 10. You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If array has only one element
        if n == 1:
            return 0
        
        # If first element is 0, we cannot move
        if arr[0] == 0:
            return -1
        
        jumps = 0
        maxReach = 0
        steps = 0
        
        for i in range(n - 1):
            maxReach = max(maxReach, i + arr[i])
            
            # When we use a jump
            if i == steps:
                jumps += 1
                steps = maxReach
                
                if steps <= i:
                    return -1
        
        return jumps
