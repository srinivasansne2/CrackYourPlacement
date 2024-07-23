class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for num in range(n):
            nums1[m+num] = nums2[num]
        nums1.sort()