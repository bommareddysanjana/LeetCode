class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for i in nums1:
            j = nums2.index(i)
            max = -1
            while j < len(nums2):
                if (nums2[j] > i):
                    max = nums2[j]
                    break;
                j+=1
            stack.append(max)
        return stack
