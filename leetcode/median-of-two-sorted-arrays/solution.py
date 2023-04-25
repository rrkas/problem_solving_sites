from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = nums1 + nums2
        new_arr.sort()
        n = len(new_arr)
        if n % 2 != 0:
            return new_arr[n // 2]
        else:
            return (new_arr[n // 2 - 1] + new_arr[n // 2]) / 2
