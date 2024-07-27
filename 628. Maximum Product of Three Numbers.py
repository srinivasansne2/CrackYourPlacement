class Solution(object):
    def maximumProduct(self, nums):
        numbers=sorted(nums)
        product1=numbers[-1]*numbers[-2]*numbers[-3]
        product2=numbers[-1]*numbers[0]*numbers[1]

        return max(product1,product2)