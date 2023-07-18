from collections import defaultdict


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # graph
    # equations[0] = [a, b]    values[0] = 2.0
    # implies following
    # a -> b    , traversing this route 2x the current value
    # b -> a    , traversing this route 1/2 x the current value
    # we can construct the graph based on this, and do dfs for each query
    # however, without memoization,
    # we could traverse same route multiple times for different query which cause the algo to be inefficient

    # memoization
    # recursive dfs
    # in each function call, record the CUR_VAR -> DESTINATION

    # TIME: O() |equations| + |variables|
    # SPACE: O() |variables|^2

    graph = defaultdict(lambda: defaultdict(lambda: -1.0))  # {var: {des: cost}}
    for i in range(len(equations)):
        a, b = equations[i]
        value = values[i]

        graph[a][b] = value
        graph[b][a] = 1 / value

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

    res = []
    for start, des in queries:
        res.append(dfs(start, des, set()))
    return res