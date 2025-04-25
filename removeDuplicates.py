def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    unique_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1
    
    return unique_index
