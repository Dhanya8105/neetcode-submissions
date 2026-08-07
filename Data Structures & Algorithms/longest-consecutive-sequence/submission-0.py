class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS=set(nums)#becoz you can see below that we search in nums a lot like if n-1 in nums and while n+length in nums....set takes o(1) tc while list takes o(n) tc to search
        longest=0
        for n in numS:
            if (n-1) not in numS:
                length=0
                while (n+length) in numS:
                    length+=1
                longest=max(length,longest)
        return longest
            