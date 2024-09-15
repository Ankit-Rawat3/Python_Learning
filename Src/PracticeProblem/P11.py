def are_anagrams(str1, str2):
    print(sorted(str1))
    print(sorted(str2))
    return sorted(str1) == sorted(str2)

# Example usage
str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
