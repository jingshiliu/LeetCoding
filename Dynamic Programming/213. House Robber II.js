const nums = [200, 3, 140, 20, 10]
console.log(rob(nums))


/**
 * @param {number[]} nums
 * @return {number}
 */
function rob(nums) {
    if (nums.length <= 3)
        return Math.max(...nums)

    return Math.max(robHouse(0, nums.length - 1), robHouse(1, nums.length))

    function robHouse(start, end) {
        let l1 = nums[start + 2] + nums[start], l2 = nums[start + 1], l3 = nums[start]

        let temp;
        for (let i = start + 3; i < end; i++) {
            temp = l1
            l1 = nums[i] + Math.max(l2, l3)
            l3 = l2
            l2 = temp
        }

        return Math.max(l1, l2)
    }
}