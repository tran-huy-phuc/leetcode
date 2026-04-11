class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            # Check if n is the starting of a sequence.
            # n is the starting number when and only wen the set does not contain (n - 1).
            if (n - 1) not in nums_set:
                # Start checking and counting: n + 1, n + 2...
                # Until n + X is not in the set -> Stop
                # -> length is the length of the sequence that starts from n
                length = 0
                while (n + length) in nums_set:
                    length += 1
                # Compare length of the current sequence (starting from n) with the longest.
                # If greater, update longest. If not, just keep the last longest as is.
                longest = max(length, longest)
        return longest 

