/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // if we want nums not be modified, we make a copy of nums array, or use 3 variables
    // to hold last 3 values

    // dynamic programming
    // the idea is that when a house is robbed, does robber want to skip 1 house, or 2 house.
    // And the reason not to skip 3 is bc we can skip 1 then skip 1 to acheive same goal and we rob one more house
    // then it's clear, that in each iteration, we check which is more of n - 2, or n - 3
    if(nums.length === 1)
        return nums[0]
    if(nums.length === 2)
        return Math.max(nums[0], nums[1])

    nums[2] += nums[0]
    for(let i = 3; i < nums.length; i++){
        nums[i] += Math.max(nums[i-2], nums[i-3])
    }
    let n = nums.length
    return Math.max(nums[n - 1], nums[n - 2])
};