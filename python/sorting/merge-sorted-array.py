# Leetcode = https://leetcode.com/problems/merge-sorted-array/

class Solution:

    def merge(self, nums1, m, nums2, n):

        for j in range(n):
            nums1[m + j] = nums2[j]
        
        self.merge_sort(nums1)

        return nums1

    def merge_sort(self, array):        

        if len(array) == 1:
            return

        mid = len(array) // 2

        left = array[:mid]

        right = array[mid:]

        self.merge_sort(left)

        self.merge_sort(right)        

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i +=1
            k +=1

        while j < len(right):
            array[k] = right[j]
            j +=1
            k +=1

solution = Solution()        

print(solution.merge([1,2,3,0,0,0], 3, [8,5,6], 3))
print(solution.merge([1], 1, [], 0))
print(solution.merge([0], 0, [1], 1))