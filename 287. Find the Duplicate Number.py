class Solution(object):
    def findDuplicate(self, nums):
        seen = {}        # A set to put the numbers we already seen
        for i in nums:     # Take all the elements of the list one by one
            if i in seen:   # If we already seen this element
                return i   # It is the repeated number !
            else:          # We haven't seen this number yet
                seen[i] = 1 # So we put it in the seen set
        return 0           # Here, we have no duplicate number, so returning 0