rain = int(input("Masukkan nilai curah hujan\t: "))

hasil = ("Cuaca terang/berawan" if rain == 0 and rain <= 0.4 else(print("Cuaca hujan ringan" if rain == 0.5 and rain <= 20 else(print("Curah hujan sedang" if rain >= 21 and rain <= 50 else(print("Curah hujan lebat" if rain == 51 and rain <= 100 else(print("Curah hujan ekstrem" if rain >= 100 else(print("Curah hujan lebat")))))))))))