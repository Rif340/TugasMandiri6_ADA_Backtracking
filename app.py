import streamlit as st
import time
from maze_draw import get_maze_draw_fig
from maze_tree import get_maze_tree_fig
from maze_solver import solve_maze_generator

st.set_page_config(page_title="Maze Solver - ADA Backtracking", layout="wide")

st.title("Tugas Mandiri 6: Analisis Desain Algoritma Pemrograman")
st.markdown("### Algoritma DFS dengan Backtracking untuk Penyelesaian Labirin")

menu = st.sidebar.selectbox(
    "Pilih Mode Visualisasi:",
    ["1. Gambar Maze", "2. Pohon Ruang Status (DFS)", "3. Simulasi DFS Solver"]
)

if menu == "1. Gambar Maze":
    st.subheader("Visualisasi Bentuk Dasar Labirin")
    fig = get_maze_draw_fig()
    st.pyplot(fig)

elif menu == "2. Pohon Ruang Status (DFS)":
    st.subheader("Pohon Ruang Status & Urutan Kunjungan")
    fig = get_maze_tree_fig()
    st.pyplot(fig)

elif menu == "3. Simulasi DFS Solver":
    st.subheader("Simulasi Penyelesaian Maze dengan DFS Backtracking")
    st.write("Klik tombol di bawah untuk memulai simulasi animasi.")
    
    start_btn = st.button("Mulai Simulasi")
    
    if start_btn:
        plot_placeholder = st.empty()
        generator = solve_maze_generator()
        
        for fig in generator:
            plot_placeholder.pyplot(fig)
            time.sleep(0.1)
        
        st.success("Simulasi selesai!")
