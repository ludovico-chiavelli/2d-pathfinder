class Node:
    def __init__(self) -> None:
        self.parent = None
        self.type = 'O'
    
    def __repr__(self) -> str:
        return f"{self.type}"
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.w = width
        self.h = height

        # Generate grid
        self.grid = [[Node() for i in range(self.w)] for j in range(self.h)]
    
    def display(self) -> None:
        for row in self.grid:
            print(row)

myGrid = Grid(5, 5)
myGrid.display()