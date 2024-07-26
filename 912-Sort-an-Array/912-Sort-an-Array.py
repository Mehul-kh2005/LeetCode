def merge_sort(array: list[int]) -> None:
    n: int = len(array)
    if n <= 1:
        return
    midle_ind: int = n // 2
    left_part: list[int] = array[:midle_ind][:]
    right_part: list[int] = array[midle_ind:][:]

    merge_sort(left_part)
    merge_sort(right_part)
    merge(left_part, right_part, array)


def merge(array1: list[int], array2: list[int], source_array: list[int]) -> None:
    p1: int = 0
    p2: int = 0
    n1: int = len(array1)
    n2: int = len(array2)
    write_ind = 0

    while p1 < n1 or p2 < n2:
        if p1 == n1 or (p2 != n2 and array2[p2] < array1[p1]):
            source_array[write_ind] = array2[p2]
            p2 += 1
        elif p2 == n2 or array1[p1] <= array2[p2]:
            source_array[write_ind] = array1[p1]
            p1 += 1
        write_ind += 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums)
        return nums