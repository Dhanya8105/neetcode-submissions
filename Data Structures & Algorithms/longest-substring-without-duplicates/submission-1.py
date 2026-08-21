class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])#here we wanna remove everything before the duplicate so while; like in abcb...we'll need two loops to remove duplicate 'b'
                l+=1
            sets.add(s[r])
            res=max(res,r-l+1)
        return res
            