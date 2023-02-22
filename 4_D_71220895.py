masukkan_nama = input("Masukkan Nama Lengkap: ")
masukkan_prodi = input("Masukkan Prodi Anda: ")
masukkan_nilai = input("Masukkan Nilai (dalam huruf) yang Anda Dapat: ")

try:
    nilai = int(masukkan_nilai)
    if nilai == 'A' :
        print("Nilai anda adlah 4.0, tbl tbl serem bgt lohh")
    elif nilai == 'A-' :
        print("Nilai anda adalah 3.75, kamu keren!")
    elif nilai == 'B+' :
        print("Nilai anda adalah 3.25, kamu sudah cukuo keren")
    elif nilai == 'B' :
        print("Nilai anda adalah 3.0, sudah bagus tingkatkan!")
    elif nilai == 'B-' :
        print("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai == 'C+' :
        print("Nilai anda adalah 2.25, jangan menyerah dan tetap semangat!!")
    elif nilai == 'C' :
        print("Nilai anda adalah 2.0, loh loh kok bisa, tapi terus berjuang aja")
    elif nilai == 'D' :
        print("Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?")
    elif nilai == 'E' :
        print("Nilai anda adalah 0, niat kuliah ngga sih???")
except:
    print("Inputan nilai yang anda masukkan tidak valid")