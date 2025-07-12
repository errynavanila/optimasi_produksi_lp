from scipy.optimize import linprog

# Fungsi objektif: Max Z = 40x + 30y → Ubah jadi Min -Z = -40x -30y
c = [-40, -30]

# Kendala:
# 2x + y ≤ 100
# x + y ≤ 80
A = [
    [2, 1],
    [1, 1]
]
b = [100, 80]

# Menyelesaikan masalah
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Tampilkan hasil
if result.success:
    print("Solusi optimal ditemukan!")
    print(f"x = {result.x[0]:.2f}")
    print(f"y = {result.x[1]:.2f}")
    print(f"Nilai maksimum Z = {-result.fun:.2f}")
else:
    print("Gagal menemukan solusi.")
    print(result.message)
