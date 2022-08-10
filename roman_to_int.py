from re import I


class Solution:
    def romanToInt(self, s: str) -> int:
        prefixed_chars = ["I", "X", "C"]
        answer = 0
        for i, c in enumerate(s):
            val = 0
            try:
                if c in prefixed_chars:
                    val = self.add_prefix(s, i)
                else:
                    val = self.get_value(c)
            except IndexError:
                val = self.get_value(c)
            print(f"{c} -> {val}")
            answer += val


        return answer
    
    def add_prefix(self, s:str, index:int):
        prefixes = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }
        if s[index+1] in prefixes[s[index]]:
            print(f"Adding prefix: {s[index]}{s[index+1]}={ -self.get_value(s[index]) + self.get_value(s[index+1]) }")
            return -self.get_value(s[index])
        else:
            return self.get_value(s[index])        
    
    def get_value(self, char):
        chars = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        return chars[char]

if __name__ == "__main__":
    solution = Solution()
    # print(solution.romanToInt("III"))
    # print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))

        