class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for num in range(n):           #Creatong for loop for len of nums2
            nums1[m+num] = nums2[num]  #Then We Replasing The nums1 values using this
        nums1.sort()                   #Then We Sorting nums1