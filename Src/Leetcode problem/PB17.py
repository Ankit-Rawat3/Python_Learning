"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""



def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string in the array as the potential common prefix
    prefix = strs[0]

    # Iterate through the rest of the strings
    for string in strs[1:]:
        # Update the prefix to be the common part of the current string and the prefix
        while not string.startswith(prefix):
            # Shorten the prefix by removing the last character until a match is found
            prefix = prefix[:-1]
            if not prefix:
                return "no common prefix"

    return prefix

# Test examples
print(longest_common_prefix(["flower", "flow", "flight"])), print(longest_common_prefix(["dog", "racecar", "car"]))
