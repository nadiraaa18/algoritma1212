import math

def hitung_akar_dan_logaritma():
  while True:
    try:
      angka = float(input("Masukkan sebuah angka positif : "))
      if angka > 0:
        break
      else:
        print("Angka harus positif. Silakan coba lagi.")
    except ValueError:
      print("Input tidak valid. Masukkan angka.")

  akar_kuadrat = math.sqrt(angka)
  logaritma_natural = math.log(angka)

  print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")
  print(f"Logaritma natural dari {angka} adalah {logaritma_natural}")

hitung_akar_dan_logaritma()
