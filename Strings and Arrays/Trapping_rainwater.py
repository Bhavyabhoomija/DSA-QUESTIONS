"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."""


class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0] * len(height)

        left[0]=height[0]
        right[len(height)-1]=height[len(height)-1]

        for i in range(1,len(height)):
            left[i]=max(left[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        water=0
        for i in range(1,len(height)-1):
            level=min(left[i],right[i])
            water+=max(0,level-height[i])
        return water
      
