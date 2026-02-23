# 1. Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
class Solution:
    def kthSmallest(self, arr, k):
        arr = sorted(arr)
        return arr[k-1]


# 2. Given an array arr[] denoting heights of n towers and a positive integer k.
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        # Initial difference
        ans = arr[n-1] - arr[0]
        
        small = arr[0] + k
        big = arr[n-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n-1):
            subtract = arr[i] - k
            add = arr[i] + k
            
            # Skip if it does not affect min or max
            if subtract >= small or add <= big:
                continue
            
            # Choose better option
            if big - subtract <= add - small:
                small = subtract
            else:
                big = add
        
        return min(ans, big - small)


# 3. Given an array arr[] denoting heights of n towers and a positive integer k.
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        # Initial difference
        ans = arr[n-1] - arr[0]
        
        small = arr[0] + k
        big = arr[n-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n-1):
            subtract = arr[i] - k
            add = arr[i] + k
            
            # Skip if it does not affect min or max
            if subtract >= small or add <= big:
                continue
            
            # Choose better option
            if big - subtract <= add - small:
                small = subtract
            else:
                big = add
        
        return min(ans, big - small)


# 4. You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
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


# 5. Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Step 1: detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: find entry point (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# 6. Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space.
#    Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.
class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)

        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap // 2) + (gap % 2)

        gap = nextGap(n + m)

        while gap > 0:
            i = 0
            j = gap

            while j < (n + m):
                if j < n and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

                elif i < n and j >= n and a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

                elif i >= n and b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

                i += 1
                j += 1

            gap = nextGap(gap)

        return a, b



# 7. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping
#   intervals that cover all the intervals in the input.
class Solution:
    def merge(self, intervals):
        # Step 1: sort intervals by start time
        intervals.sort()
        
        merged = []
        
        for interval in intervals:
            # If merged list empty OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping → merge
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged



# 8. Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no 
#    such elements return an empty array. In this case, the output will be -1.
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        
        result = []
        
        while i < n1 and j < n2 and k < n3:
            
            # If all three are equal → common element
            if arr1[i] == arr2[j] == arr3[k]:
                # Avoid duplicates
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            
            # Move the smallest pointer forward
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        if not result:
            return [-1]
        
        return result


# 9. Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.
class Solution:
    def factorial(self, n):
        res = [1]   # stores digits
        
        for x in range(2, n + 1):
            carry = 0
            
            for i in range(len(res)):
                val = res[i] * x + carry
                res[i] = val % 10
                carry = val // 10
            
            while carry:
                res.append(carry % 10)
                carry //= 10
        
        res.reverse()
        return res


# 10. Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
class Solution:
    def isSubset(self, a, b):
        freq = {}
        
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        for num in b:
            if freq.get(num, 0) == 0:
                return False
            freq[num] -= 1
        
        return True


# 11. Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
#     Return true if such a triplet exists, otherwise, return false.
class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        arr.sort()
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                
                if total == target:
                    return True
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return False


# 12. Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between
#     the blocks during the rainy season.
class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        
        left_max = 0
        right_max = 0
        water = 0
        
        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water 


