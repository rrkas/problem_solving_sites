class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to keep track of the characters seen so far
        char_dict = {}
        # Initialize pointers for the sliding window
        left, right = 0, 0
        # Initialize the maximum length seen so far
        max_len = 0
        # Iterate over the string
        while right < len(s):
            # If the current character is not in the dictionary, add it and move the right pointer
            if s[right] not in char_dict:
                char_dict[s[right]] = right
                right += 1
            else:
                # If the current character is in the dictionary, remove the leftmost character and move the left pointer
                del char_dict[s[left]]
                left += 1
            # Update the maximum length seen so far
            max_len = max(max_len, right - left)
        return max_len


# improved the almost solution using ChatGPT
