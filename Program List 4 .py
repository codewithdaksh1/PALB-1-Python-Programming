# 1. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        
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


# 2. Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You
#    may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of 
#    the chosen numbers is different. The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
class Solution:
    def combinationSum(self, candidates, target):
        
        result = []
        
        def backtrack(start, current, total):
            
            if total == target:
                result.append(current[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # i (not i+1)
                current.pop()
        
        backtrack(0, [], 0)
        return result


# 3. Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#    Each number in candidates may only be used once in the combination.
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])  # i+1 (use once)
                path.pop()

        backtrack(0, [], 0)
        return res


# 4. You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0. Each element nums[i] represents the maximum length of a forward jump from index i.
#    In other words, if you are at index i, you can jump to any index (i + j) where:
#  • 0 <= j <= nums[i] and
#  • i + j < n
#    Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
class Solution:
    def jump(self, nums):

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


# 5. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict

        mp = defaultdict(list)

        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-97] += 1
            mp[tuple(count)].append(word)

        return list(mp.values())


# 6. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least 
#    significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.
class Solution:
    def plusOne(self, digits):
        
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits


# 7. Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
class Solution:
    def setZeroes(self, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Use first row & col as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0



# 8. You are given an m x n integer matrix matrix with the following two properties:
#    • Each row is sorted in non-decreasing order.
#    • The first integer of each row is greater than the last integer of the previous row.
#    Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            row = mid // n
            col = mid % n
            
            val = matrix[row][col]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# 9. Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#   We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.
class Solution:
    def sortColors(self, nums):
        
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1



# 10. Given an integer array nums of unique elements, return all possible subsets (the powerset). The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums):
        
        res = []
        subset = []
        
        def backtrack(start):
            res.append(subset[:])  
            
            for i in range(start, len(nums)):
                subset.append(nums[i])      
                backtrack(i + 1)            
                subset.pop()                
        
        backtrack(0)
        return res



# 11. Given an m x n grid of characters board and a string word, return true if word exists in the grid.
class Solution:
    def exist(self, board, word):
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  \
            
            found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            
            board[r][c] = temp  
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False


# 12. Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#  • 0 <= a, b, c, d < n
#  • a, b, c, and d are distinct.
#  • nums[a] + nums[b] + nums[c] + nums[d] == target
#  You may return the answer in any order.
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return result


# 13. There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly left rotated at an unknown index k 
#     (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
#     nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # left half sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # right half sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


# 14. Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#    If target is not found in the array, return [-1, -1].
class Solution:
    def searchRange(self, nums, target):
        
        def findFirst():
            left, right = 0, len(nums) - 1
            first = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    first = mid
                    right = mid - 1   # move left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return first
        
        def findLast():
            left, right = 0, len(nums) - 1
            last = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    last = mid
                    left = mid + 1   # move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return last
        
        return [findFirst(), findLast()]
