# Aritmatika

angka_1 = int(input("Masukan angka pertama: "))
angka_2 = int(input("Masukan angka kedua: "))

penjumlahan = angka_1 + angka_2
pengurangan = angka_1 - angka_2
perkalian = angka_1 * angka_2
pembagian = angka_1 / angka_2
modulus = angka_1 % angka_2
pangkat = angka_1 ** angka_2
pem_bulat = angka_1 // angka_2

print(f'{angka_1} + {angka_2} = ', penjumlahan)
print(f'{angka_1} - {angka_2} = ', pengurangan)
print(f'{angka_1} x {angka_2} = ', perkalian)
print(f'{angka_1} / {angka_2} = ', pembagian)
print(f'{angka_1} % {angka_2} = ', modulus)
print(f'{angka_1} pangkat {angka_2} = ', pangkat)
print("Hasil pem. bulat = ", pem_bulat)
