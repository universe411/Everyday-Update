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
        # needcode说确实要比较s和t的length长度 但他和我想法不一样
        # #他是在最开始比较之后 如果不同直接return false
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for i in range(len(s)):
            # 用get，如果s[i]的value在countS里，那么就+1，如果没有，那么return default value 0
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[s[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t
