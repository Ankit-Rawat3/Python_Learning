"""Ransom Note Easy Topics Companies Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
a=input("Enter ransomeNote string : \n ")
b=input("Enter magazine string : \n")

if a in b:
    print(True)
    print(b[-1:1])
else:
    print(False)

"""a="ankit"
b=a[::-1]
print(b)
"""