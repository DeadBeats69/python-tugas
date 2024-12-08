import os

def clear_screen():
    # Membersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')

nama = input("Masukkan Nama     : ")

# Validasi input NPM
while True:
    npm = input("Masukkan NPM      : ")
    if npm.isdigit():  # Memastikan input hanya berisi angka
        break
    else:
        print("NPM harus berupa angka. Silakan coba lagi.")

kelas = input("Masukkan Kelas    : ")
jurusan = input("Masukkan Jurusan  : ")
fakultas = input("Masukkan Fakultas : ")

# Membersihkan layar setelah input selesai
clear_screen()

# Menampilkan data mahasiswa
print("Data Mahasiswa")
print("Nama     : ", nama)
print("NPM      : ", npm)
print("Kelas    : ", kelas)
print("Jurusan  : ", jurusan)
print("Fakultas : ", fakultas)
