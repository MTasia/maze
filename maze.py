from collections import deque


def possible_neighbours(i, j, maze, we_were):
    neighbours = []
    if not on_border(j, i, maze):
        if maze[i + 1][j] == 1 and not we_were[i + 1][j]:
            neighbours.append((i + 1, j))
        if maze[i][j + 1] == 1 and not we_were[i][j + 1]:
            neighbours.append((i, j + 1))
        if maze[i - 1][j] == 1 and not we_were[i - 1][j]:
            neighbours.append((i - 1, j))
        if maze[i][j - 1] == 1 and not we_were[i][j - 1]:
            neighbours.append((i, j - 1))
    return neighbours


def on_border(i, j, maze):
    return j == 0 or i == 0 or j == len(maze[0]) - 1 or i == len(maze) - 1


def count_step_to_exit(maze, j, i):
    we_were = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    dist = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    queue = deque()
    queue.append((i, j))
    while queue:
        we_in = queue.popleft()
        we_were[we_in[0]][we_in[1]] = True
        neighbours = possible_neighbours(we_in[0], we_in[1], maze, we_were)
        if len(neighbours) == 0 and not queue:
            return 0
        for neighbour in neighbours:
            dist[neighbour[0]][neighbour[1]] = dist[we_in[0]][we_in[1]] + 1
            queue.append(neighbour)
            if on_border(neighbour[0], neighbour[1], maze):
                return dist[neighbour[0]][neighbour[1]]


def main():
    maze = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]
    x, y = 1, 1
    step = count_step_to_exit(maze, x, y)
    print(step)


if __name__ == '__main__':
    main()
