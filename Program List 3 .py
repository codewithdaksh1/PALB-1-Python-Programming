# 1. Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number
#     of chocolates. There are m students, the task is to distribute chocolate packets among m students such that :
# i). Each student gets exactly one packet.
# ii). The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and 
#     return that minimum possible difference.
class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        if m == 0 or n == 0:
            return 0
        
        if m > n:
            return -1
        
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff


# 2. Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do 
#    not exist return 0 in that case.
class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        
        min_len = n + 1
        curr_sum = 0
        left = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > x:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1
        
        if min_len == n + 1:
            return 0
        
        return min_len


# 3. Given an array and a range a, b. The task is to partition the array around the range such that the array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.
class Solution:
    def threeWayPartition(self, arr, a, b):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
                
            elif arr[mid] > b:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                
            else:
                mid += 1
        
        return True


# 4. Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index 
#    i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal
#    to k together, i.e. make them a contiguous subarray.
class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: count good elements
        good = 0
        for num in arr:
            if num <= k:
                good += 1
        
        # Step 2: count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        # Step 3: slide the window
        i = 0
        j = good
        
        while j < n:
            # remove left element
            if arr[i] > k:
                bad -= 1
                
            # add right element
            if arr[j] > k:
                bad += 1
                
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans


# 5. Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.
def isPalinArray(arr):
    
    for num in arr:
        temp = num
        rev = 0
        
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        
        if rev != num:
            return False
    
    return True


# 6. Given an array arr[] of integers, calculate the median.
class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n//2 - 1] + arr[n//2]) / 2


# 7. You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.
class Solution:
    def spirallyTraverse(self, mat):
        
        res = []
        
        top = 0
        bottom = len(mat) - 1
        left = 0
        right = len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            
            # left → right
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1
            
            # top → bottom
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
            
            if top <= bottom:
                # right → left
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            
            if left <= right:
                # bottom → top
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
        
        return res


# 8. You are given an m x n integer matrix matrix with the following two properties:
# • Each row is sorted in non-decreasing order.
# • The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in 
#   matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.
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


# 9. Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.
import bisect

class Solution:
    def median(self, mat):
        
        n = len(mat)
        m = len(mat[0])
        
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        desired = (n * m) // 2
        
        while low < high:
            mid = (low + high) // 2
            
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid
        
        return low


# 10. You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order.
#     Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.
class Solution:
    def rowWithMax1s(self, arr):

        if not arr:
            return -1

        n = len(arr)
        m = len(arr[0])

        row = 0
        col = m - 1
        ans = -1

        while row < n and col >= 0:
            if arr[row][col] == 1:
                ans = row
                col -= 1   # move left
            else:
                row += 1   # move down

        return ans
