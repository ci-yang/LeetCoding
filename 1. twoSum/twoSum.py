class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        print(nums)
        for i in range(len(nums)):
            match = -1
            remain = target - nums[i]
            print("i: ", i)
            print("remain: ", remain)
            for c in range(i+1, len(nums)):
                print(nums[c])
                if( remain - nums[c] == 0 ):
                    print("c: ", c)
                    match = c
                    break
            if(match is not -1):
                result.append(i)
                result.append(match)
                break

        return result
        

c = Solution()
x = c.twoSum([-1,-2,-3,-4,-5], -8)
#x = c.twoSum([0,4,3,0], 0)
#x = c.twoSum([2,7,11,13], 9)
print(x)