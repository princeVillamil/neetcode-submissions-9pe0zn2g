class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sLetters = {}
        for letter in s:
            sLetters[letter] = sLetters[letter]+1 if letter in sLetters else 1
        print(sLetters)
        for letter in t:
            if letter not in sLetters or sLetters[letter] == 0: return False
            sLetters[letter] = sLetters[letter] - 1
        return True