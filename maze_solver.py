import matplotlib.pyplot as plt
from matplotlib.patches import Patch

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

start = (2, 0)
finish = (10, 12)

rows = len(maze)
cols = len(maze[0])

def solve_maze_generator():
    visited = set()
    path = []
    
    fig, ax = plt.subplots(figsize=(10, 8))

    def draw_wall_line(ax, x1, y1, x2, y2):
        ax.plot([x1, x2], [y1, y2], color="#2D3748", linewidth=4.5, solid_capstyle="round")

    def draw_maze(current=None):
        ax.clear()
        ax.set_xlim(-0.5, cols + 0.5)
        ax.set_ylim(rows + 0.5, -0.5)
        ax.set_aspect("equal")
        ax.axis("off")
        
        fig.patch.set_facecolor("#F7FAFC")
        ax.set_facecolor("#F7FAFC")

        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 0:
                    ax.add_patch(plt.Rectangle((c, r), 1, 1, facecolor="#FFFFFF", edgecolor="#E2E8F0", linewidth=0.5))

        for r, c in visited:
            ax.add_patch(plt.Rectangle((c + 0.15, r + 0.15), 0.7, 0.7, facecolor="#FEEBC8", alpha=0.85))

        for r, c in path:
            ax.add_patch(plt.Rectangle((c + 0.15, r + 0.15), 0.7, 0.7, facecolor="#C6F6D5", alpha=0.9))

        sr, sc = start
        ax.add_patch(plt.Rectangle((sc + 0.1, sr + 0.1), 0.8, 0.8, facecolor="#805AD5", edgecolor="#553C9A", linewidth=1.5, label="Start"))
        ax.text(sc + 0.5, sr + 0.5, "S", color="white", weight="bold", ha="center", va="center", fontsize=12)

        fr, fc = finish
        ax.add_patch(plt.Rectangle((fc + 0.1, fr + 0.1), 0.8, 0.8, facecolor="#D69E2E", edgecolor="#975A16", linewidth=1.5, label="Finish"))
        ax.text(fc + 0.5, fr + 0.5, "F", color="white", weight="bold", ha="center", va="center", fontsize=12)

        if current is not None:
            r, c = current
            ax.add_patch(plt.Rectangle((c + 0.2, r + 0.2), 0.6, 0.6, facecolor="#E53E3E", edgecolor="#9B2C2C", linewidth=1.5))

        draw_wall_line(ax, 0, 0, cols, 0)
        draw_wall_line(ax, 0, rows, cols, rows)
        draw_wall_line(ax, 0, 0, 0, 2)
        draw_wall_line(ax, 0, 3, 0, rows)
        draw_wall_line(ax, cols, 0, cols, rows - 1)

        for r in range(rows):
            for c in range(cols):
                if maze[r][c] != 0:
                    continue
                if r == 0 or maze[r-1][c] == 1:
                    draw_wall_line(ax, c, r, c+1, r)
                if r == rows-1 or maze[r+1][c] == 1:
                    draw_wall_line(ax, c, r+1, c+1, r+1)
                if (c == 0 and r != 2) or (c > 0 and maze[r][c-1] == 1):
                    draw_wall_line(ax, c, r, c, r+1)
                if (c == cols-1 and r != 10) or (c < cols-1 and maze[r][c+1] == 1):
                    draw_wall_line(ax, c+1, r, c+1, r+1)

        legend_elements = [
            Patch(facecolor="#805AD5", label="Start (S)"),
            Patch(facecolor="#D69E2E", label="Finish (F)"),
            Patch(facecolor="#C6F6D5", label="Solusi Aktif (Active Path)"),
            Patch(facecolor="#FEEBC8", label="Dikunjungi (Visited)"),
            Patch(facecolor="#E53E3E", label="Posisi DFS Sekarang")
        ]
        ax.legend(handles=legend_elements, loc="upper center", bbox_to_anchor=(0.5, -0.02), ncol=3, frameon=True, facecolor="#FFFFFF", edgecolor="#E2E8F0")

        status_text = "Mencari Jalur..." if current != finish else "Solusi Ditemukan!"
        ax.set_title(f"DFS Maze Solver - {status_text}\nNode Dikunjungi: {len(visited)}", fontsize=14, pad=15, weight="bold", color="#2D3748")

    def dfs(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols: return False
        if maze[x][y] == 1: return False
        if (x, y) in visited: return False

        visited.add((x, y))
        path.append((x, y))

        draw_maze((x, y))
        yield fig

        if (x, y) == finish:
            yield True
            return True

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                for step in dfs(nx, ny):
                    if step is True:
                        yield True
                        return True
                    yield step

        path.pop()
        draw_maze((x, y))
        yield fig

        return False

    for step in dfs(start[0], start[1]):
        if step is True:
            break
        yield step

    draw_maze(finish)
    yield fig
