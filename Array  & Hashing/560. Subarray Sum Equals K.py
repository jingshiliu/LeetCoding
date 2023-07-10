def subarray_sum(nums, k):
    """
    Time: O(n)
    Space: O(n)

    cum_sum[i] - cum_sum[j] means the sum of subarray between j and i

    using a hashmap to record the cumulative sum of each step before
    hashmap = cumulative_sum : number_of_occurence

    in each iter, the difference of currrent sum and K is the cum_sum that required to appear before to form a subarray sum of K

    there might be multiple occurence of some cum_sum, so we record the occurence_times as value of hashmap
    and add that value to 'res'
    """
    cum_sum = {0: 1}
    cur = 0
    res = 0
    for n in nums:
        cur += n
        diff = cur - k
        if diff in cum_sum:
            res += cum_sum[diff]

        if cur in cum_sum:
            cum_sum[cur] += 1
        else:
            cum_sum[cur] = 1

    return res