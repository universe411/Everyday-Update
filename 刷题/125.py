"""

Valid Palindrome
Solved 
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''  # 定义一个新的空字符串，之后会加入清洗过的字符
        # 用一个for loop 遍历原来字符串s里的每个字符 c是当前处理的character
        for c in s:
            if c.isalnum():  # 返回true说明是英文字母或数字 返回false说明是空格表点符号
                newStr += c.lower()  # 如果当前字符是字母或数字，就把它转成小写后加到 newStr 里
        return newStr == newStr[::-1]
        # 比较clean之后的字符串是否等于它的反转版
        # [::-1] 表示从头到尾倒序取字符串
        # "abc"[::-1] → "cba"
