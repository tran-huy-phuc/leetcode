class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        output = [1] * nums_len
        
        prefix = 1
        # Product of all numbers before i
        for i in range(nums_len):
            output[i] = prefix
            prefix *= nums[i]
        print(output)

        suffix = 1
        for i in range(nums_len - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        print(output)

        return output

        