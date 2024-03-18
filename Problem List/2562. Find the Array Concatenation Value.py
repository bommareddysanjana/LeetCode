class Solution(object):
    def findTheArrayConcVal(self, nums):
        left, right, total = 0, len(nums) - 1, 0
        while left <= right:
            if left < right:
                total += int(str(nums[left])+str(nums[right]))
            else:
                total += nums[left]
            left += 1
            right -= 1
        return total
