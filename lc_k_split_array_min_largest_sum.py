'''
https://leetcode.com/problems/split-array-largest-sum/description/

Split array into K parts such that maximum sum in the parts is minimized.
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        class Test:
            def __getitem__(self, index: int) -> bool:
                splits = [0]
                for n in nums:
                    if splits[-1]+n>index:
                        splits.append(0)
                    splits[-1] += n
                return len(splits) <= k
        
        test = Test()
        lo, hi = max(nums), sum(nums)
        return bisect.bisect_left(test, True, lo, hi)
