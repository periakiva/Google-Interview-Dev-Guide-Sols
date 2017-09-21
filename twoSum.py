class Solution:
    def twoSum(self,nums,target):
        co = []
        try:
            for i in xrange(0,len(nums)+1):
                if nums[i] in co:
                    return [co.index(nums[i]),i]
                else:
                    co.insert(len(co),target-nums[i])
                    print co
        except IndexError:
            return None

nums = [2,7,11,15,50,12,33,2,43,2,7]
print nums
target = 45
a = Solution()
print a.twoSum(nums,target)
