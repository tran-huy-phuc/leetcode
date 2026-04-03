class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            numI = nums[i]
            if (numI in numsDict.keys()):
                return [numsDict[numI], i]
            numsDict[target - numI] = i
        return []