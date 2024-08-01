class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()                    #Creating a empty seen set for seprate
        duplicates = []                 #Creating Empty list to store duplicates
        for num in nums:                #Geting The no one by one using for loop
            if num in seen:             #Then Checking The Num Is in seen
                duplicates.append(num)  #If its already in seen wee adding the no into duplicate list
            else:                       #Else its not in a seen
                seen.add(num)           #then we adding into seen
        return duplicates               #After the for loop completion We Returning the duplicates