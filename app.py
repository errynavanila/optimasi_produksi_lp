import streamlit as st
from scipy.optimize import linprog

st.set_page_config(page_title="Optimasi Produksi", layout="centered")

st.title("🎯 Optimasi Produksi Linear Programming")
st.markdown("## Maksimalkan Z = 40x + 30y")
st.markdown("### Dengan kendala:")
st.latex(r"""
\begin{aligned}
2x + y &\leq 100 \\
x + y &\leq 80 \\
x, y &\geq 0
\end{aligned}
""")

if st.button("🔍 Hitung Solusi Optimal"):
    c = [-40, -30]
    A = [[2, 1], [1, 1]]
    b = [100, 80]

    result = linprog(c, A_ub=A, b_ub=b, method='highs')

    if result.success:
        x, y = result.x
        z = 40*x + 30*y
        st.success("✅ Solusi Ditemukan!")
        st.write(f"**x = {x:.2f}**")
        st.write(f"**y = {y:.2f}**")
        st.write(f"**Nilai Maksimum Z = {z:.2f}**")
    else:
        st.error("❌ Gagal menemukan solusi.")
