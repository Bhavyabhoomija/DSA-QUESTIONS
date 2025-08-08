from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        while len(nums) < 2:
            return len(nums)
        count=1
        i=1
        while i < len(nums):
            if nums[i-1]==nums[i]:
                count+=1
                if count ==3:
                    nums.pop(i)
                
                    count-=1
                    i-=1
            else:
                count=1
            i+=1
            
            
   """
   method 2
   """
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        write=2
        for read in range(2,len(nums)):
            if nums[read]!=nums[write-2]:
                nums[write]=nums[read]
                write+=1
        return write

           
                
                
     
