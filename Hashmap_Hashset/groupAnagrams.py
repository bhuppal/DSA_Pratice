def groupAnagramsBruteforce(strs: list[str]) -> list[list[str]]:
    n = len(strs)
    visited = [False] * n
    result = []

    for i in range(n):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and isAnagram(strs[i], strs[j]):
                group.append(strs[j])
                visited[j] = True
        result.append(group)
    return result

def groupAnagramsSol1(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

def groupAnagramsSol2(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1
        key = tuple(count)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

def isAnagram(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)





strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

print(groupAnagramsBruteforce(strs))
print(groupAnagramsSol1(strs))
print(groupAnagramsSol2(strs))
