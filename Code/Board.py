# Board.py: Backend zum 4-Gewinnt
# von Leon und Marcel

from Slot import Slot
import GewinnBerechnung


# Player 1 = 1
# Player 2 = 2
# Empty slot = 0
class Board:
    WinsPlayer1 = 0  # Variable zum Zählen der Anzahl, der gewonnen Spiele von Spieler 1
    WinsPlayer2 = 0  # Variable zum Zählen der Anzahl, der gewonnen Spiele von Spieler 2

    """
    Initialize the Board with a height and a width
    """

    def __init__(self, x_width, y_height):
        self.x_width = x_width    # definiert wie breit das Feld ist
        self.y_height = y_height  # definiert wie hoch das Feld ist

        self.slots = {}

        # Dictionary self.slots:
        # Key: Position als Tuple (x, y)
        # Value: Slot Instanz aus Slot.py [Slot()]
        for y in range(1, (self.y_height + 1)):  # erstellt die einzelnen Slots (Felder)
            for x in range(1, (self.x_width + 1)):
                self.slots[x, y] = Slot((x, y), 0)
        
        # Slot Instanz:
        # Attribut 1: Position
        # Attribut 2: Status (0, 1, 2)

    def zaehler(self, status):
        # 
        if status == 1:
            Board.WinsPlayer1 += 1
        if status == 2:
            Board.WinsPlayer2 += 1

    def changeStatus(self, position: tuple, status):
        try:
            self.slots[
                position].status = status  # ändert den Status eines Feldes → der Chip des jeweiligen Spielers besetzt das Feld
        except KeyError:
            print("Position not found!")

    def getLowestFree(self, x):
        for y in reversed(range(1, self.y_height + 1)):
            if self.slots[x, y].status == 0:
                return x, y
    
    def won(self, status, wonChips):
        self.zaehler(status)
        return wonChips

    def checkIfWon(self, position, status):
        # return GewinnBerechnung.gewinn_berechnen(self.slots, position)
        
        wonChips = []  # erstellt eine Liste, in der die Slots gespeichert werden, die zum Sieg geführt haben
        numberOfChips = 0  # eine Variable zum Zählen, wie viele Chips eines Spielers schon hintereinader gefolgt sind
        # Senkrecht
        x, notUseY = position
        for y in range(1, (
                self.y_height + 1)):  # geht die x Reihe (senkrecht) komplet durch, dabei bleibt der x Wert gleich
            if self.slots[x, y].status == status:
                numberOfChips += 1  # erhöht der Chip-Counter um jeweils 1
                wonChips.append(
                    self.slots[x, y])  # fügt der Liste wonChips die "Daten" des Slots zu, der zu der Reihe beiträgt
            else:
                if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                    return self.won(status, wonChips)
        
                numberOfChips = 0  # falls die Reihe unterbrochen ist, wird der counter, der die Chipreihe zählt, wieder auf 0 gesetzt
                wonChips = []  # leert die Liste mit den Daten der Slots
        if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
            return self.won(status, wonChips)

        # Waagerecht
        wonChips = []
        numberOfChips = 0
        notUseX, y = position
        for x in range(1, (self.x_width + 1)):
            if self.slots[x, y].status == status:
                numberOfChips += 1
                wonChips.append(self.slots[x, y])
            else:
                if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                    return self.won(status, wonChips)
                numberOfChips = 0
                wonChips = []
        if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
            return self.won(status, wonChips)

        # Diagonal
        wonChips = []
        numberOfChips = 0
        currentX, currentY = position
        while (currentX > 1) and (currentY > 1):
            currentX -= 1
            currentY -= 1

        while currentX < self.x_width and currentY < self.y_height:
            if self.slots[currentX, currentY].status == status:
                numberOfChips += 1
                wonChips.append(self.slots[currentX, currentY])
            else:
                if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                    return self.won(status, wonChips)
                numberOfChips = 0
                wonChips = []

            currentX += 1
            currentY += 1

        if self.slots[currentX, currentY].status == status:
            numberOfChips += 1
            wonChips.append(self.slots[currentX, currentY])
        else:
            if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                return self.won(status, wonChips)
            numberOfChips = 0
            wonChips = []
        if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
            return self.won(status, wonChips)

        # For the other direction
        wonChips = []
        numberOfChips = 0
        currentX, currentY = position
        while (currentX < self.x_width) and (currentY > 1):
            currentX += 1
            currentY -= 1

        while currentX > 1 and currentY < self.y_height:
            if self.slots[currentX, currentY].status == status:
                numberOfChips += 1
                wonChips.append(self.slots[currentX, currentY])
            else:
                if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                    return self.won(status, wonChips)
                numberOfChips = 0
                wonChips = []

            currentX -= 1
            currentY += 1

        if self.slots[currentX, currentY].status == status:
            numberOfChips += 1
            wonChips.append(self.slots[currentX, currentY])
        else:
            if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
                return self.won(status, wonChips)
            numberOfChips = 0
            wonChips = []
        if numberOfChips >= 4:  # wenn der counter größer oder gleich 4 ist, wird die Liste wonChips ausgegeben
            return self.won(status, wonChips)


if __name__ == "__main__":
    board = Board(6, 7)
    for key in board.slots.keys():
        print(str(key) + ": " + str(board.slots[key].status))

    board.changeStatus((1, 1), 1)
    board.changeStatus((2, 2), 1)
    board.changeStatus((3, 3), 1)
    board.changeStatus((4, 4), 1)

    print(board.checkIfWon((1, 1), 1))

    board = Board(6, 7)

    board.changeStatus((1, 1), 2)
    board.changeStatus((2, 1), 2)
    board.changeStatus((3, 1), 2)
    board.changeStatus((4, 1), 2)
    # print(board.getLowestFree(3))

    print(board.checkIfWon((1, 1), 2))
    print(Board.WinsPlayer1)
    print(Board.WinsPlayer2)
