class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        build=None
        abbr_lst = []
        for i,c in enumerate(abbr):
            if build == 0: return False
            if build==None:
                if c.isdigit(): build = int(c)
                else: build = c
            else:
                if c.isdigit(): tmp=int(c)
                else: tmp = c
                if type(tmp) == type(build):
                    if isinstance(build,int):
                        build = build*10 + int(c)
                    else: build+=c
                else:
                    abbr_lst.append(build)
                    build=tmp
        abbr_lst.append(build)

        i = 0
        for item in abbr_lst:
            if isinstance(item, int):
                i += item
                if i > len(word):  # Overshooting the word length
                    return False
            else:
                # if i + len(item) > len(word) or word[i:i + len(item)] != item:
                if i + len(item) > len(word) or word[i + len(item)-1] != item[len(item)-1]:
                    return False
                i += len(item)

        # Ensure the entire word is consumed
        return i == len(word)

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0  # Pointers for word and abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':  # Leading zero is invalid
                    return False

                # Extract the full number from abbr
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                # Skip num characters in word
                i += num
            else:
                # Check if the current character matches
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Both word and abbr must be fully traversed
        return i == len(word) and j == len(abbr)
