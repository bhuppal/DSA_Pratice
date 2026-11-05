def lexicographicalSequenceChar(s: list[int]) -> str:
    letters = list(s)
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1

    if pivot == -1:
        print('ddd')
        return letters[::-1]

    right_successor = len(s) - 1
    while letters[right_successor] <= letters[pivot]:
        right_successor -= 1

    letters[right_successor], letters[pivot] = letters[pivot], letters[right_successor]

    letters[pivot + 1:] = reversed(letters[pivot + 1:])
    return letters

# s = "ynitsed" # output = "ynsdeit
'''
v [0]
n [1]
i [2]
t [3]
s [4]
e [5]
d [6]
'''
# s = "dcba"
arr = [3, 2, 1]
print(lexicographicalSequenceChar(arr))