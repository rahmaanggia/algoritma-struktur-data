list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah)

# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

# ubah data dalam range
list_buah[1:3] = ['Naga', 'Pepaya']
print(list_buah)

# tambah data di belakang list
list_buah.append('Sirsak')
print(list_buah)

# tambah data di awal list
list_buah.insert(0, 'Jambu')
print(list_buah)

# tambah data di index mana pun dalam list
list_buah.insert(2, 'Manggis')
print(list_buah)