class Solution:
    res = []

    def isPal(self, word):
        # Check palindrome
        return word == word[::-1]

    def backtrack(self, idx, tmp, s):
        # If we used the full string, add partition
        if idx == len(s):
            self.res.append(tmp.copy())
            return

        # Try all substring cuts
        for j in range(idx, len(s)):
            word = s[idx:j+1]
            if self.isPal(word):
                tmp.append(word)
                self.backtrack(j + 1, tmp, s)
                tmp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backtrack(0, [], s)
        return self.res