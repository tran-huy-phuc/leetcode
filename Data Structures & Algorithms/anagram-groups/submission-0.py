class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            # List to count occurrences of each letter from a to z.
            # Intialize it with 26 zeros because the alphabet has 26 letters
            alphabet_count = [0] * 26 

            # Loop through each character of the string.
            # Update the occurrences in [alphabet_count]
            for c in s:
                alphabet_count[ord(c) - ord("a")] += 1

            alphabet_count_key = tuple(alphabet_count)
            # Create an item with key = [alphabet_count_key] if not existing
            if alphabet_count_key not in result:
                result[alphabet_count_key] = []

            # Add [s] to the values (list) of the item with key = alphabet_count_key
            result[alphabet_count_key].append(s)

        return list(result.values())