import asyncio


class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wonChips = []

        self.slots: dict[tuple, int] = {}
        for y in range(1, (self.y + 1)):
            for x in range(1, (self.x + 1)):
                self.slots[x, y] = 0

    async def getLowestFreeSlot(self, x) -> tuple:
        for y in reversed(range(1, self.y + 1)):
            if self.slots[x, y] == 0:
                return x, y

    async def changeStatus(self, position: tuple, status: int):
        self.slots[position] = status

    async def horizontal_L(self, position: tuple, status: int) -> list:
        for pos in range(position[0]):
            if self.slots[position] == status:
                self.wonChips.append(position)


    async def horizontal_R(self, position: tuple, status: int) -> list:


    async def checkWin(self, position: tuple, status: int) -> list:
        pass

    """
    match point:
    case():
    """


if __name__ == "__main__":
    import time
    s = time.perf_counter()

    board = Board(7, 6)
    print(board.slots)

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    #asyncio.run(main())
