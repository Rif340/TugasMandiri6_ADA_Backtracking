import matplotlib.pyplot as plt

def get_maze_draw_fig():
    maze = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    ]

    rows = len(maze)
    cols = len(maze[0])

    fig, ax = plt.subplots(figsize=(8, 7))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    ax.set_xlim(-0.2, cols + 0.2)
    ax.set_ylim(rows + 0.2, -0.2)
    ax.set_aspect("equal")
    ax.axis("off")

    def draw_wall_line(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color="black", linewidth=4.5, solid_capstyle="butt")

    draw_wall_line(0, 0, cols, 0)
    draw_wall_line(0, rows, cols, rows)
    draw_wall_line(0, 0, 0, 2)
    draw_wall_line(0, 3, 0, rows)
    draw_wall_line(cols, 0, cols, rows - 1)

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != 0:
                continue
            if r == 0 or maze[r-1][c] == 1:
                draw_wall_line(c, r, c+1, r)
            if r == rows-1 or maze[r+1][c] == 1:
                draw_wall_line(c, r+1, c+1, r+1)
            if (c == 0 and r != 2) or (c > 0 and maze[r][c-1] == 1):
                draw_wall_line(c, r, c, r+1)
            if (c == cols-1 and r != 10) or (c < cols-1 and maze[r][c+1] == 1):
                draw_wall_line(c+1, r, c+1, r+1)

    plt.tight_layout()
    return fig
