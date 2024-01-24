class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        r1 = "qwertyuiopQWERTYUIOP"
        r2 = "asdfghjklASDFGHJKL"
        r3 = "zxcvbnmZXCVBNM"
        for word in words:
            flag = 0
            flag = (
                all(char in r1 for char in word)
                or all(char in r2 for char in word)
                or all(char in r3 for char in word)
            )
            if flag:
                res.append(word)
        return res
