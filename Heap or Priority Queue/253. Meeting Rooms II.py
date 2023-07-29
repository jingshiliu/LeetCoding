from heapq import heapify, heappop, heappush


def min_meeting_rooms2(intervals):
    # Time: O(nlogn), O(nlogn) for sorting intervals, and heappush and pop for N times with each take O(logn)
    # Space: O(n), the variable or res, rooms, which can store up to N ints
    # sort the intervals
    # manage the ending time of rooms using a min heap
    # min_heap[0] is the earliest ending time to use an occupied room
    # if cur_start > heap[0], meaning no room is available before the start of current interval
    # so we have to get a new room

    # Also note when min_heap[0] = 10 and cur_start = 20,
    # it's impossible that there is another room can fit into the gap between min_heap[0] and cur_start
    # because intervals is been sorted, and cur_start is always the earliest unassigned interval
    # and there will never be a cur_start after 20 smaller than 20
    # Thus, this algo always minimizing the gap between last end and next start

    intervals.sort()
    rooms = [intervals[0][1]]  # initialize with the ending time of earliest interval

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if rooms[0] <= start:
            heappop(rooms)

        heappush(rooms, end)

    return len(rooms)


def min_meeting_rooms_1(intervals):
    # heapify the intervals, from smallest start time to largest
    # pop one meeting at a time, find a room that has closest ending time
    # we can have a rooms LIST, iterate the list every time needs to find a closest ending time
    # Time: O(n * (n + logn)) O(n) for finding closest, O(logn) for popping heap, doing this N times
    # Space: O(n)
    heapify(intervals)
    rooms = []  # store the ending times
    while intervals:
        cur_start, cur_end = heappop(intervals)
        room_end, room_index = cur_start, -1
        for i, end in enumerate(rooms):
            if end <= room_end:
                room_end = end
                room_index = i
        if room_index >= 0:
            rooms[room_index] = cur_end
        else:
            rooms.append(cur_end)
    return len(rooms)