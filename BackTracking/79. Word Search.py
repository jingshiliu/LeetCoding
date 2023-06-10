class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRow = len(board)
        numCol = len(board[0])
        visited = set()

        def findLetter(index, coordinate):
            if index == len(word):
                return True

            r, c = coordinate

            if (coordinate in visited or
                    not (0 <= r < numRow) or
                    not (0 <= c < numCol) or
                    board[r][c] != word[index]):
                return

            visited.add(coordinate)

            if findLetter(index + 1, (r + 1, c)) or findLetter(index + 1, (r - 1, c)) or findLetter(index + 1, (
            r, c + 1)) or findLetter(index + 1, (r, c - 1)):
                return True

            visited.remove(coordinate)

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if findLetter(0, (i, j)):
                    return True

        return False


