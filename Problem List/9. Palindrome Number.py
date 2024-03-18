class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        while copy:
            remainder = copy % 10
            reverse = (reverse * 10) + remainder
            copy = copy // 10
        return x == reverse
