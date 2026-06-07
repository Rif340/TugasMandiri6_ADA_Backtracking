import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def get_maze_tree_fig():
    tree_nodes = {
        1: {'cell': (2, 0), 'type': 'Start', 'label': '1', 'coord_str': '(2,0)'},
        2: {'cell': (0, 4), 'type': 'Junction', 'label': '2', 'coord_str': '(0,4)'},
        3: {'cell': (2, 6), 'type': 'DeadEnd', 'label': '3', 'coord_str': '(2,6)'},
        4: {'cell': (4, 4), 'type': 'Junction', 'label': '4', 'coord_str': '(4,4)'},
        5: {'cell': (4, 2), 'type': 'Junction', 'label': '5', 'coord_str': '(4,2)'},
        6: {'cell': (10, 2), 'type': 'DeadEnd', 'label': '6', 'coord_str': '(10,2)'},
        7: {'cell': (10, 6), 'type': 'DeadEnd', 'label': '7', 'coord_str': '(10,6)'},
        8: {'cell': (4, 8), 'type': 'Junction', 'label': '8', 'coord_str': '(4,8)'},
        9: {'cell': (0, 10), 'type': 'Junction', 'label': '9', 'coord_str': '(0,10)'},
        10: {'cell': (0, 12), 'type': 'DeadEnd', 'label': '10', 'coord_str': '(0,12)'},
        11: {'cell': (10, 12), 'type': 'Finish', 'label': '11', 'coord_str': '(10,12)'},
        12: {'cell': (8, 10), 'type': 'DeadEnd', 'label': '-', 'coord_str': '(8,10)'},
        13: {'cell': (8, 6), 'type': 'DeadEnd', 'label': '-', 'coord_str': '(8,6)'},
        14: {'cell': (2, 2), 'type': 'DeadEnd', 'label': '-', 'coord_str': '(2,2)'}
    }

    tree_edges = {
        1: [2, 14], 2: [3, 4], 4: [5, 8, 13],
        5: [6, 7], 8: [9, 12], 9: [10, 11]
    }

    node_positions = {
        1: (0, 5), 2: (-1.5, 4), 14: (1.5, 4), 3: (-2.5, 3), 4: (-0.5, 3),
        5: (-1.5, 2), 8: (0.5, 2), 13: (1.5, 2), 6: (-2.2, 1), 7: (-0.8, 1),
        9: (0.2, 1), 12: (1.2, 1), 10: (-0.3, 0), 11: (0.7, 0)
    }

    fig, ax = plt.subplots(figsize=(11, 9))
    fig.patch.set_facecolor('#F7FAFC')
    ax.set_facecolor('#F7FAFC')

    for parent, children in tree_edges.items():
        px, py = node_positions[parent]
        for child in children:
            cx, cy = node_positions[child]
            ax.plot([px, cx], [py, cy], color='#A0AEC0', linewidth=2.5, zorder=1)

    for node_id, pos in node_positions.items():
        x, y = pos
        info = tree_nodes[node_id]
        ntype = info['type']
        
        if ntype == 'Start':
            color, edge_color = '#805AD5', '#553C9A'
        elif ntype == 'Finish':
            color, edge_color = '#D69E2E', '#975A16'
        elif ntype == 'Junction':
            color, edge_color = '#48BB78', '#276749'
        else:
            color, edge_color = '#E53E3E', '#9B2C2C'
            
        ax.add_patch(plt.Circle((x, y), 0.2, facecolor=color, edgecolor=edge_color, linewidth=2, zorder=2))
        ax.text(x, y, info['label'], color='white', weight='bold', fontsize=11, ha='center', va='center', zorder=3)
        ax.text(x + 0.25, y, info['coord_str'], color='#4A5568', fontsize=9, ha='left', va='center', zorder=3)

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    legend_elements = [
        Patch(facecolor='#805AD5', label='Pintu Masuk (Start)'),
        Patch(facecolor='#D69E2E', label='Pintu Keluar (Finish)'),
        Patch(facecolor='#48BB78', label='Persimpangan (Junction)'),
        Patch(facecolor='#E53E3E', label='Jalan Buntu (Dead End)')
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.01), ncol=4, frameon=True, facecolor='#FFFFFF', edgecolor='#E2E8F0', fontsize=10)

    plt.title("POHON RUANG STATUS & URUTAN KUNJUNGAN DFS\n(Prioritas Eksplorasi: Kiri, Atas, Kanan, Bawah)", fontsize=14, pad=20, weight='bold', color='#2D3748')
    plt.tight_layout()
    return fig
