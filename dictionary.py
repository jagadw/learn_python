mahasiswa = {
    "nama": "Krisna",
    "NIM" : "210010062",
    "Prodi" : "SK"
}

# Menampilkan seluruh pasangan key-value
for key,value in mahasiswa.items():
    print(f"{key}: {value}")

print(mahasiswa["nama"])

# Menambahkan key-value terbaru
mahasiswa["Jenis_Kelamin"] = True

# Menghapus data key-value
del mahasiswa["prodi"]