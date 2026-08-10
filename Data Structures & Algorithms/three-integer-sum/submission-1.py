class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
                #skips everyything afther this; since there is nothing here moves to i+1
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=a+nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                        #incase the number l is pointing to repeats again..here when l cant be duplicated and neither can i be so there is no question of res having duplicates..we dont really check for r duplicates
        return res