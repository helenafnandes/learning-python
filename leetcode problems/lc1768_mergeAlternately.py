class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ''
        if len(word1) < len(word2):
            for i in range(len(word1)):
                word3 += word1[i]
                word3 += word2[i]
            for i in range(len(word1), len(word2)):
                word3 += word2[i]
        else:
            for i in range(len(word2)):
                word3 += word1[i]
                word3 += word2[i]
            for i in range(len(word2), len(word1)):
                word3 += word1[i]
        return word3