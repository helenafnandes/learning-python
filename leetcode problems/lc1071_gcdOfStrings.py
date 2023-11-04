class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        str3 = ""
        gdc = 0
        a = 0
        b = 0
        if len(str1) > len(str2):
            for i in range(1, len(str2) + 1):
                if len(str1) % i == 0 and len(str2) % i == 0:
                    gdc = i

            for i in range(gdc):
                if str1[i] == str2[i]:
                    str3 += str1[i]
                    a = i
                else:
                    break

            for i in range(a, len(str1)):
                if not str3[b] == str1[a + 1]:
                    str3 = ""
                    break
        return (str3)