class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        nums_len = len(nums)
        for i in range(nums_len):
            product = 1
            for j in range(nums_len):
                if j != i:
                    product *= nums[j]
            output.append(product)
        return output