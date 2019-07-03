class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos1, pos2 = 0, len(numbers)-1
        
        while pos1 < pos2:
            sum = numbers[pos1] + numbers[pos2]
            if sum < target:
                pos1 += 1
            elif sum > target:
                pos2 -= 1
            else:
                return [pos1 + 1, pos2 + 1]
        
        return []
