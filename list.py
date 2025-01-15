mix_list = [False, 1, 2, 3, "Empat", "Lima"]

mix_list.append(['a','b','c']) # Memasukkan data di list terakhir
mix_list.insert(1, True) # Memasukan data di index ke-1
mix_list[3] = 7 # Mengedit data di index ke -3
mix_list.pop(1) # Menghapus data list index terakhir
# del mix_list[2] # Menghapus data di index ke-2

print(mix_list)