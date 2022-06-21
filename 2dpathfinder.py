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
    nodes = cameFrom.keys()
    while curr in nodes:
        curr = cameFrom[curr]
        nodes.remove(curr)
    return path.reverse()


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
        
        # check neighbors
        neighbors = [
            (curr_n[0] - 1, curr_n[1] - 1), # top left
            (curr_n[0], curr_n[1] - 1), # above
            (curr_n[0] + 1, curr_n[1] - 1), # top right
            (curr_n[0] - 1, curr_n[1]), # left
            (curr_n[0] + 1, curr_n[1]), # right
            (curr_n[0] - 1, curr_n[1] + 1), # bottom left
            (curr_n[0], curr_n[1] + 1), # below
            (curr_n[0] + 1, curr_n[1] + 1), # bottom right
        ]
        
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
    print(pathfinder(myGrid, (0, 0), (9, 9), heuristic))