def can_visit_all_rooms(rooms: list[list]) -> bool:
    N = len(rooms)
    stack, visited = [0], set()
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue

        visited.add(cur)
        if len(visited) == N:
            return True

        for key in rooms[cur]:
            stack.append(key)
    return False