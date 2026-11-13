def isAnagram(s: str, t: str) -> bool:
    hashMapS = {}
    for x in s:
        hashMapS[x] = hashMapS.get(x, 0) + 1

    print(hashMapS)

    for x in t:
        hashMapS[x] = hashMapS.get(x, 0) - 1

    print(hashMapS)

    for v in hashMapS.values():
        if v != 0:
            return False
    
    return True

s = "racecar"
t = "carrace"
print(isAnagram(s, t))
