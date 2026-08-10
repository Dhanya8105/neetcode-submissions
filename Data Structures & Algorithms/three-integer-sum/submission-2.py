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
                    r-=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                        #here instead of moving l duplicates like in previous code i am moving r duplicates...do not forget to move r first before finding the duplicates in r
        return res