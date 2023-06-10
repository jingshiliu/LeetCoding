def singleNumber(nums) -> int:
    ans = 0
    for i in nums:
        ans ^= i
    return ans

# a ^ 0 = a
# a ^ a = 0
# a ^ b ^ a = a ^ a ^ b = 0 ^ b = b
