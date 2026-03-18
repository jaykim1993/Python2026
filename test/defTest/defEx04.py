nums = [15, 3, 24, 8, 42, 10]
min = nums[0]
max = nums[0]
def find_min_max(nums):
    global min, max
    for num in nums:
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)

resultMin , resultMax = find_min_max(nums)
print(f"최대값: {resultMax}, 최소값: {resultMin}")