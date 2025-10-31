class Solution:
    def isPalindrome(self, x: str) -> bool:
        ls=[]
        for i in x:
            if i.isalnum():
                ls.append(i.lower())
        return ls==ls[::-1]