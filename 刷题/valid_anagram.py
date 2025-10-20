"""

Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, 
otherwise return false.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
    """


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s和t的长度要一样 然后每个字母的字数得一样 然后创建dictionary 查找？
        if len(s) == len(t):
            number_s = {}, number_t = {}
