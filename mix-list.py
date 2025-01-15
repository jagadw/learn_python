mix_list = [False,1,2,3, "empat","lima"]

mix_list.append(['a','b','c']) # Memasukkan data di list terakhir
mix_list.insert(1,True) # Memasukkan data di index ke-1
mix_list[3] = 8 # Mengedit data pada index ke-3
mix_list.pop(1) #menghapus data list index terakhir
del mix_list[2] # Menghapus Data di index ke-2 

print (mix_list)

