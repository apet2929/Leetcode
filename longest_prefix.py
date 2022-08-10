class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            letter = ""
            for s in strs:
                try:
                    if letter == "":
                        letter = s[i]
                    else:
                        if s[i] != letter:
                            return prefix
                except IndexError:
                    return prefix

            prefix += letter
        return prefix


if __name__ == "__main__":
    solution = Solution()
    # print(solution.romanToInt("III"))
    # print(solution.romanToInt("LVIII"))
    strs = ["dog","racecar","car"]
    print(solution.longestCommonPrefix(strs))

    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))