from math import ceil


def carFleet(self, target: int, position, speed) -> int:
    cars = [[position[i], speed[i]] for i in range(len(position))]  # O(N)
    cars.sort(reverse=True)  # O(nlog n)
    stack = []

    for pos, s in cars:  # O(N)
        stack.append((target - pos) / s)  # This calculates the time to reach target

        # If the car behind takes less time to reach the target
        # that means, at some point before target, the car behind must intersect with the front car
        # However, the car behind cannot pass through front car so they form a fleet

        # If they reach the target at the same time, they form a fleet
        # We only track fleets, so we pop()
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)  # Overall, O(nlogn)


# -------------------------------------------------------
# A slight improved version, without using stack

def carFleet2(target, position, speed) -> int:
    cars = [[position[i], speed[i]] for i in range(len(position))]  # O(N)
    cars.sort(reverse=True)  # O(nlog n)
    res, cur = 0, 0

    for pos, s in cars:  # O(N)
        if not (target - pos) / s <= cur:  # This calculates the time to reach target
            cur = (target - pos) / s
            res += 1
        # If the car behind takes less time to reach the target
        # that means, at some point before target, the car behind must intersect with the front car
        # However, the car behind cannot pass through front car so they form a fleet

        # If they reach the target at the same time, they form a fleet
        # We only track fleets, so we pop()

    return res  # Overall, O(nlogn)







def carFleet3(target, position, speed) -> int:
    cars = [(position[i], speed[i]) for i in range(len(position))]
    cars.sort()
    print(cars)
    # [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
    time = [(target - pos) / speed for pos, speed in cars]
    print(time)
    # [12, 3, 7, 1, 1]
    fleets = 1
    cur = time[-1]
    for t in reversed(time):
        if t > cur:
            fleets += 1
            cur = t
    return fleets





























target = 10
position = [8,3,7,4,6,5]

speed = [4,4,4,4,4,4]
print(carFleet3(target, position, speed))






































