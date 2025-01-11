def firstUniqChar(self, s: str) -> int:
        repeating = set()
        for i in range(len(s)):
            if s[i] in s[i+1:] or s[i] in repeating:
                repeating.add(s[i])
            else:
                return i
        return -1