from collections import defaultdict


def check_contradiction(equations, values):
    """
    DFS

    """
    DIFF_ALLOWED = 0.00001
    graph = defaultdict(lambda: defaultdict(lambda: -1.0))  # {var: {des: cost}}

    def dfs(cur, des, visited):
        if cur not in graph or des not in graph:
            return -1.0
        if graph[cur][des] > 0:
            return graph[cur][des]

        visited.add(cur)
        value = -1.0
        for next_node in graph[cur].keys():
            if next_node in visited or graph[cur][next_node] < 0:
                continue
            graph[cur][des] = graph[cur][next_node] * dfs(next_node, des, visited)
            if graph[cur][des] > 0:
                value = graph[cur][des]
            else:
                graph[cur][des] = -1.0
        return value

    for i in range(len(equations)):
        a, b = equations[i]
        value = values[i]

        if a == b:
            if value != 1:
                return True
            graph[a][b] = value
            continue

        if a in graph and b in graph:
            true_value = dfs(a, b, set())
            if true_value > 0 and abs(true_value - value) > DIFF_ALLOWED:
                return True

        graph[a][b] = value
        graph[b][a] = 1 / value

    return False