from collections import defaultdict


def path_sum(root, target_sum):
    """
    Time: O(n)
    Space: O(n)
    """
    def dfs(node, sum_occurence_map: defaultdict, last_sum: int, k: int):
        if not node:
            return 0

        cur_sum = last_sum + node.val
        sum_start = cur_sum - k
        path_found = 0
        if sum_occurence_map[sum_start] > 0:
            path_found += sum_occurence_map[sum_start]

        sum_occurence_map[cur_sum] += 1
        path_found += dfs(node.left, sum_occurence_map, cur_sum, k)
        path_found += dfs(node.right, sum_occurence_map, cur_sum, k)
        sum_occurence_map[cur_sum] -= 1
        return path_found

    sum_occurrence_map = defaultdict(lambda: 0)
    sum_occurrence_map[0] = 1
    return dfs(root, sum_occurrence_map, 0, target_sum)