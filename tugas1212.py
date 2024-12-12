import math

def hitung_hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# contoh penggunaan
sisi_a = 3
sisi_b = 4
hipotenusa = hitung_hipotenusa(sisi_a, sisi_b)
print(f"panjang hipotenusa adalah: {hipotenusa}")
