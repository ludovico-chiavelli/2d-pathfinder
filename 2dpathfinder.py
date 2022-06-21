import heapq
import math

class Node:
    def __init__(self) -> None:
        self.marker = 'O'
    
    def __repr__(self) -> str:
        return f"{self.marker}"
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        # Generate grid
        self.grid = [[Node() for i in range(self.width)] for j in range(self.height)]
    
    def addObstacle(self, coord: tuple):
        x, y = coord[0], coord[1]
        self.grid[y][x].marker = 'X'
    
    def display(self) -> None:
        for row in self.grid:
            print(row)

def heuristic(curr_coord: tuple, dest_coord: tuple) -> int:
    """Manhattan heuristic for estimating distance from current node to destination node

    Args:
        curr_coord (tuple): coordinate of current node
        dest_coord (tuple): coordinate of destination node

    Returns:
        int: estimated distance to destination node
    """
    return (abs(dest_coord[0] - curr_coord[0]) * 10) + (abs(dest_coord[1] - curr_coord[1]) * 10)

def reconstruct_path(cameFrom: dict, curr: tuple) -> list:
    path = []
    nodes = list(cameFrom.keys())
    while curr in nodes:
        path.append(curr)
        nodes.remove(curr)
        curr = cameFrom[curr]
    path.reverse()
    return path

def find_neighbors(curr_n: tuple, max_x: int, max_y: int) -> list:
    neighbors = []
    for j in range(curr_n[1] - 1, curr_n[1] + 2):
        for i in range(curr_n[0] - 1, curr_n[0] + 2):
            neigh = (i, j)
            blocked = [curr_n[0], curr_n[1], -1, max_x, max_y]
            if neigh[0] not in blocked and neigh[1] not in blocked:
                neighbors.append(neigh)
    return  neighbors
    


def pathfinder(grid: Grid, start: tuple, dest: tuple, heuristic) -> None:
    # min-heap of nodes that needs to be expanded
    openList = []
    heapq.heappush(openList, start)

    # dictionary to keep track of shortest path
    cameFrom = {start: None}

    allCoords = []
    for y in range(grid.height):
        for x in range(grid.width):
            allCoords.append((x,y))
    gScore = dict.fromkeys(allCoords, math.inf)
    gScore[start] = 0

    fScore = dict.fromkeys(allCoords, math.inf)
    fScore[start] = heuristic(start, dest)

    while len(openList) != 0:
        curr_n = heapq.heappop(openList)

        if curr_n == dest:
            return reconstruct_path(cameFrom, curr_n)
        
        neighbors = find_neighbors(curr_n, grid.width, grid.height)

        for neighbor in neighbors:
            # calc distance from curr to neighbor
            if curr_n[0] == neighbor[0] or curr_n[1] == neighbor[1]: # the neighbor is on the same column or row
                d = 10
            else:
                d= 14
            tentative_gScore = gScore[curr_n] + d

            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = curr_n
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + heuristic(neighbor, dest)
                if neighbor not in openList:
                    heapq.heappush(openList, neighbor)
    return -1

if __name__ == "__main__":
    myGrid = Grid(10, 10)

    # add in obstacles
    myGrid.addObstacle((9, 7))
    myGrid.addObstacle((8, 7))
    myGrid.addObstacle((7, 7))
    myGrid.addObstacle((7, 8))

    myGrid.display()

    print(pathfinder(myGrid, (0, 0), (9, 9), heuristic))