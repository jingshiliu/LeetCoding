class TimeMap:
    # timestamp_prev < timestamp in same key
    # i use hashmap, and each key's value is another hashmap which the key is timestamp
    # since timestampList(timeMap.key.timestamp) is sorted by default
    # we use bin search to find the timestamp N such that
    # N <= timestamp < N+1

    # Note that dict.keys() returns a view list which contents cannot be accessed like an array
    # so I need to create a timestampList to do that
    # however, if we do list(dict.keys()) everytime in get(), it's too expensive
    # therefore, we store a timestampList in the key's val hashmap

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = {'timestampList': []}
        self.timeMap[key][timestamp] = value
        self.timeMap[key]['timestampList'].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ''
        timestampList = self.timeMap[key]['timestampList']
        if timestamp >= timestampList[-1]:
            return self.timeMap[key][timestampList[-1]]
        if timestamp < timestampList[0]:
            return ''

        l, r = 1, len(timestampList)

        while l < r:
            cur = (l + r) // 2
            if timestampList[cur] > timestamp >= timestampList[cur - 1]:
                return self.timeMap[key][timestampList[cur - 1]]
            elif timestampList[cur] > timestamp:
                r = cur
            else:
                l = cur + 1

        return self.timeMap[key][timestampList[r]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)