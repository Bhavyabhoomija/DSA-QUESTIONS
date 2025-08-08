"""
169
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=Counter(nums)

        for i in count:
            if count[i] > n//2:
                return i
        
