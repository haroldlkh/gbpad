class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        i = 0
        n = len(s)

        # Step 1: Parse the string into groups
        while i < n:
            if s[i] == '{':
                i += 1  # Skip '{'
                group = []
                while s[i] != '}':
                    if s[i] != ',':
                        group.append(s[i])
                    i += 1
                groups.append(sorted(group))  # Sort to maintain lexicographical order
            else:
                groups.append([s[i]])  # Treat single characters as a group
            i += 1  # Move past '}' or regular character

        # Step 2: Generate combinations via backtracking
        result = []
        
        def backtrack(index, path):
            if index == len(groups):
                # result.append("".join(path))
                result.append(path)
                return
            for char in groups[index]:
                # backtrack(index + 1, path + [char])
                backtrack(index + 1, path + char)

        backtrack(0, '')
        return result


# Complexity Analysis

# Parsing the Input:
# O(N) where N is the length of s.

# Generating Words:
# There are O(k^m) possible words, where:

# k is the average size of each group.
# m is the number of groups.
# Backtracking runs in O(k^m) and stores O(k^m) words.

# 🔹 Total Complexity: O(N + k^m)
