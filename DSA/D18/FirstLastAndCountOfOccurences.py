"""
Problem: First and last occurences and count of occurences 
Approach: Binary Search
TC: O(log n)
SC: O(1)

"""
class Solution:
    def count_occurences(self, arr, target):
        first = self.find_first_occurence(arr, target)
        if first == -1:
            return 0
        last = self.find_last_occurence(arr, target)
        return last - first + 1

    def find_first_occurence(self, arr, target):
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result
    
    def find_last_occurence(self, arr, target):
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result   


sol = Solution()
arr = [1, 2, 2, 2, 3, 4, 5]
print(f"Count of occurrences: {sol.count_occurences(arr, 2)}") 