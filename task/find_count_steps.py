from collections import deque


def on_border(n_rows, n_cols, point):
    """
    Parameters:
    :n_rows (int): x-shape
    :n_cols (int): y-shape
    :point (tuple): point with x and y for check
    :return: bool value that tells whether a point is on the border
    """
    i = int(point[0])
    j = int(point[1])
    return 0 == i or i == n_rows - 1 or 0 == j or j == n_cols - 1


def possible_neighbours(point):
    """
    Parameters:
    :point (tuple): point with x and y for possible neighbours
    :return: list of nearby neighbors for point
    """
    neighbours = []
    x = point[1]
    y = point[0]
    neighbours.append((x, y + 1))
    neighbours.append((x + 1, y))
    neighbours.append((x, y - 1))
    neighbours.append((x - 1, y))
    return neighbours


def count_steps(start, end, prev_step_map):
    """
   Parameters:
   :start (tuple): start point with x and y
   :end (tuple): end point
   :prev_step_map(dict): the dictionary with previous step map
   :return: count steps
   """


def count_steps_to_exit(maze, start):
    """
    Parameters:
   :maze (list([])): the matrix with 0 and 1
   :start (tuple): start point with x and y
   :return: count steps
   """
    j = start[0]
    i = start[1]
    we_were = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    dist = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    queue = deque()
    queue.append((i, j))
    while queue:
        we_in = queue.popleft()
        we_were[we_in[0]][we_in[1]] = True
        neighbours = need_neighbours(we_in[0], we_in[1], maze, we_were)
        if len(neighbours) == 0 and not queue:
            return 0
        for neighbour in neighbours:
            dist[neighbour[0]][neighbour[1]] = dist[we_in[0]][we_in[1]] + 1
            queue.append(neighbour)
            point = (neighbour[0], neighbour[1])
            if on_border(len(maze), len(maze[0]), point):
                step = dist[neighbour[0]][neighbour[1]]
                if step != 0:
                    step += 1
                return step


def need_neighbours(i, j, maze, we_were):
    neighbours = []
    point = (j, i)
    if not on_border(len(maze), len(maze[0]), point):
        if maze[i + 1][j] == 1 and not we_were[i + 1][j]:
            neighbours.append((i + 1, j))
        if maze[i][j + 1] == 1 and not we_were[i][j + 1]:
            neighbours.append((i, j + 1))
        if maze[i - 1][j] == 1 and not we_were[i - 1][j]:
            neighbours.append((i - 1, j))
        if maze[i][j - 1] == 1 and not we_were[i][j - 1]:
            neighbours.append((i, j - 1))
    return neighbours
