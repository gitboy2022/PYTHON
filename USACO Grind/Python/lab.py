# ignore this file
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            num = int(arr[i])
            one_after = int(arr[i+1])
            two_after = int(arr[i+2])
            print(num, one_after, two_after)
            if num % 2 != 0 and one_after % 2 != 0 and two_after % 2 != 0:
                return True
        return False
    