class Node:
    def __init__(self) -> None:
        self.parent = None
        self.marker = 'O'
    
    def __repr__(self) -> str:
        return f"{self.marker}"
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.w = width
        self.h = height

        # Generate grid
        self.grid = [[Node() for i in range(self.w)] for j in range(self.h)]
    
    def display(self) -> None:
        for row in self.grid:
            print(row)


if __name__ == "__main__":
    myGrid = Grid(5, 5)
    myGrid.display()