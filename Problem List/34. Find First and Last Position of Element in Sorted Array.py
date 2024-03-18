class Solution(object):
    def searchRange(self, nums, target):
        p = []
        for i in range(len(nums)):
            if nums[i] == target:
                p.append(i)
        if len(p) == 0:
            p.append(-1)
            p.append(-1)
            return p
        else:
            p1 = []
            p1.append(min(p))
            p1.append(max(p))
            return p1
