class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        nums_len = len(nums)
        # 1st approach: Brute-force: O(n^2)
        # for i in range(nums_len):
        #     product = 1
        #     for j in range(nums_len):
        #         if j != i:
        #             product *= nums[j]
        #     output.append(product)
        # return output

        # 2nd approach
        total_product = 1
        zero_count = 0
        for i in range(nums_len):
            if (nums[i] != 0):
                total_product *= nums[i]
            else:
                zero_count += 1

        for i in range(nums_len):
            if (nums[i] == 0):
                if (zero_count == 1):
                    output.append(total_product)
                else:
                    output.append(0)
            else:
                if (zero_count >= 1):
                    output.append(0)
                else:
                    output.append(int(total_product/nums[i]))

        return output