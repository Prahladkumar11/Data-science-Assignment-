def firstUniqChar(str) :
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    
    return -1

s = "leetcode"
print(firstUniqChar(s))
