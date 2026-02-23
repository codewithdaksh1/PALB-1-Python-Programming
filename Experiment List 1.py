# You are given an array of integers arr[]. You have to reverse the given array.
class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        return arr
