class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [[] for _ in range(numRows)]

        rev = False
        count = -1

        for c in s:
            if not rev:
                count += 1
            else:
                count -= 1

            strings[count].append(c)

            if count == numRows - 1:
                rev = True
            elif count == 0:
                rev = False

        zigzag = ""

        for string in strings:
            zigzag += "".join(string)

        return zigzag
