class RandomizedSet:

    def __init__(self):
        self.valToIndex = {}
        self.array = []

    def insert(self, val: int) -> bool:  # O(1)
        if val in self.valToIndex:
            return False
        self.array.append(val)
        self.valToIndex[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:  # O(1)
        if val not in self.valToIndex:
            return False

        # this is the index of the value we are removing]
        index = self.valToIndex[val]
        lastElement = self.array[-1]

        if self.array[index] != lastElement:
            # swap it with the last element, and then pop it
            self.array[index], self.array[-1] = self.array[-1], self.array[index]

            # update the index in hashMap if its not the last element in the array
            self.valToIndex[lastElement] = index
        self.array.pop()
        self.valToIndex.pop(val)

        return True

    def getRandom(self) -> int:  # O(1)
        return random.choice(self.array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()