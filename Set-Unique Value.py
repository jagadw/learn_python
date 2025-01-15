# Set, Unique Value 
set1 = {1,2,3,4,5,5}
set2 = {4,5,6,7,8}

set1.add(10)  #Menambahkan elemen ke set
set1.remove(2) # Menghapus elemen dari set

gabungan = set1.union(set2) # Mengabungkan set1 & set2
persamaan = set1.intersection(set2) # irisan set1 & set2
perbedaan = set1.difference(set2) # selisih set1 & set2

print(gabungan)